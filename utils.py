import librosa
import torch
import torchvision
from torchvision.transforms import v2
import torchaudio
import cv2
from math import ceil
import os
from tqdm import tqdm
from typing import Sequence

from logger import log
import warnings
warnings.filterwarnings("ignore")


@log(msg='splitting video into frames and audio')
def split_stream(filepath: str | os.PathLike,
                 step: int = 1e3,
                 frame_size: int = 448,
                 sample_rate: int = 16e3,
                 half_precision: bool = True) ->\
                    tuple[torch.Tensor, torch.Tensor]:
    """Splits video into tensor of images and tensor of sound samples

    Args:
        filepath (str | os.PathLike): Path where video is stored.
        step (int, optional): Step by which frames are extracted from video in milliseconds. Defaults to 1e3.
        frame_size (int, optional): Frame size to crop original frames. Defaults to 448.
        sample_rate (int, optional): Sample rate for audio. Defaults to 16e3.
        half_precision (bool, optional): Encode sound samples with half precision. Defaults to True.

    Raises:
        FileNotFoundError: If videofile not found at given filepath

    Returns:
        (video, audio) (tuple[torch.Tensor, torch.Tensor):
        Tensor of Images (mode=RGB), tensor of sound samples
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'File not found at {filepath}')
    
    audio_array, sr = librosa.load(filepath)
    audio = torch.from_numpy(audio_array)
    audio = (torchaudio.transforms.Resample(orig_freq=sr, new_freq=sample_rate)(audio)).\
        to(dtype=(torch.float16 if half_precision else torch.float32))

    cap = cv2.VideoCapture(filepath)
    duration = (cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS))
    total_frames = ceil(duration / (step / 1e3))
    video = torch.empty(size=(total_frames, 3, frame_size, frame_size), dtype=torch.uint8)

    transforms = torchvision.transforms.Compose([
        v2.ToPILImage(),
        v2.Resize(512),
        v2.CenterCrop(frame_size),
        v2.ToImage(),
        v2.ToDtype(dtype=torch.uint8, scale=True)
        ])

    frame_count, pos = 0, 0
    while cap.isOpened():
        cap.set(cv2.CAP_PROP_POS_MSEC, pos)
        ret, frame = cap.read()
        if not ret:
            break
        
        video[frame_count] = transforms(frame)
        frame_count += 1
        pos += step
    
    cap.release()
    return (video, audio)


@log(msg='getting tensors of frames and audio for given videos')
def get_batch(filepaths: Sequence[str | os.PathLike],
              step: int = 0.5e3,
              frame_size: int = 448,
              sample_rate: int = 16e3,
              half_precision: bool = True) ->\
                tuple[torch.Tensor, torch.Tensor]:
    """Getting image and sound tensors

    Args:
        filepaths (str | os.PathLike): Paths where video is stored.
        step (int, optional): Step by which frames are extracted from videos in milliseconds. Defaults to 1e3.
        frame_size (int, optional): Frame size to crop original frames. Defaults to 448.
        sample_rate (int, optional): Sample rate for audio. Defaults to 16e3.
        half_precision (bool, optional): Encode sound samples with half precision. Defaults to True.

    Raises:
        FileNotFoundError: If videofile not found at given filepath

    Returns:
        (video_tensors, audio_tensors) (tuple[torch.Tensor, torch.Tensor):
        Tensor of Image tensors (mode=RGB), tensor of sound sample tensors
    """
    audio_tensors, video_tensors = list(), list()
    for fp in tqdm(filepaths):
        video, audio = split_stream(fp, step=step, frame_size=frame_size, sample_rate=sample_rate, half_precision=half_precision)
        video_tensors.append(video)
        audio_tensors.append(audio)

    return (torch.stack(video_tensors), torch.nn.utils.rnn.pad_sequence(audio_tensors).T)
