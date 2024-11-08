from moviepy.editor import VideoFileClip, AudioFileClip
import numpy as np
from math import ceil
import cv2
from PIL import Image
import os
from logger import log


@log(msg='splitting video into frames and audio')
def split_stream(filepath: str | os.PathLike,
                 step: int = 1e3,
                 sample_rate: int = 16e3,
                 half_precision: bool = True) ->\
                    tuple[np.ndarray[Image.Image], np.ndarray[np.ndarray[np.float16 | np.float32]]]:
    """Splits video into array of images and audiostream.

    Args:
        filepath (str | os.PathLike): Path where video is stored.
        step (int, optional): Step by which frames are extracted from video in milliseconds. Defaults to 1e3.
        sample_rate (int, optional): Sample rate for audio. Defaults to 16e3.
        half_precision (bool, optional): Encode sound samples with half precision. Defaults to True.

    Raises:
        FileNotFoundError: If videofile not found at given filepath

    Returns:
        (video, audio) (tuple[np.ndarray[Image.Image], np.ndarray[np.ndarray[np.float16 | np.float32]]]):
        Array of PIL.Images, audio represented as array of souns samples
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'File not found at {filepath}')
    
    with VideoFileClip(filepath) as clip:
        audio = clip.audio.to_soundarray(fps=sample_rate, nbytes=(2 if half_precision else 4)).\
            astype(dtype=(np.float16 if half_precision else np.float32))

    cap = cv2.VideoCapture(filepath)
    duration = (cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS))
    total_frames = ceil(duration / (step / 1e3))
    video = np.empty(shape=(total_frames), dtype=Image.Image)

    frame_count, pos = 0, 0
    while cap.isOpened():
        cap.set(cv2.CAP_PROP_POS_MSEC, pos)
        ret, frame = cap.read()
        if not ret:
            break
        
        video[frame_count] = Image.fromarray(frame)
        frame_count += 1
        pos += step
    
    cap.release()       
    return (video, audio)
