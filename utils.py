import librosa
import torch
import torchaudio
import cv2
from math import ceil
import os
from tqdm import tqdm
from typing import Sequence
from functools import partial
from logger import log
import warnings
warnings.filterwarnings("ignore")


@log(msg='splitting video into frames and audio')
def split_stream(filepath: str | os.PathLike,
                 step: int = 1e3,
                 sample_rate: int = 16e3,
                 half_precision: bool = True) ->\
                    tuple[torch.Tensor, torch.Tensor]:
    """Splits video into array of images and audiostream.

    Args:
        filepath (str | os.PathLike): Path where video is stored.
        step (int, optional): Step by which frames are extracted from video in milliseconds. Defaults to 1e3.
        sample_rate (int, optional): Sample rate for audio. Defaults to 16e3.
        half_precision (bool, optional): Encode sound samples with half precision. Defaults to True.

    Raises:
        FileNotFoundError: If videofile not found at given filepath

    Returns:
        (video, audio) (tuple[np.ndarray[Image.Image], torch.Tensor[torch.float16 | torch.float32]]):
        Array of PIL.Images, audio represented as array of souns samples
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
    height, width = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video = torch.empty(size=(total_frames, height, width, 3), dtype=torch.uint8)

    frame_count, pos = 0, 0
    while cap.isOpened():
        cap.set(cv2.CAP_PROP_POS_MSEC, pos)
        ret, frame = cap.read()
        if not ret:
            break
        
        video[frame_count] = torch.from_numpy(frame)
        frame_count += 1
        pos += step
    
    cap.release()
    return (video, audio)



for i in ['a', 'b', 'c', 'd', 'e']:
    split_stream(f'{i}.mp4')


@log(msg='getting tensors of frames and audio for given videos')
def get_batch(filepaths: Sequence[str | os.PathLike],
              step: int = 0.5e3,
              half_precision: bool = True):
    sample_rate = 16e3

    audio_tensors, video_tensors = list(), list()
    for fp in tqdm(filepaths):
        video, audio = split_stream(fp, step=step, sample_rate=sample_rate, half_precision=half_precision)
        video_tensors.append(video)
        audio_tensors.append(audio)

    pad_type = 'constant'
    pad = partial(torch.nn.functional.pad,
                    pad=(1, max(tensor.size(-1)
                                for tensor in audio_tensors)),
                    mode=pad_type,
                    value=0.0)
    return (video_tensors, torch.stack([pad(audio) for audio in audio_tensors], dim=0))
