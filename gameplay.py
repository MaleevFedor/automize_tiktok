import moviepy.editor as mpy
from moviepy.video import fx
from random import randint


def prepare_gameplay(length=60, res=(1920, 1080)):
    clip = mpy.VideoFileClip("files/gta_gameplay.mp4")
    start_time = randint(15, int(clip.duration) - 16 - length)
    clip = clip.subclip(start_time, start_time+length)
    #clip = clip.resize(2)
    #ToDo work with every resolution
    (w, h) = clip.size
    cropped_clip = fx.all.crop(clip, width=1080, height=960, x_center=w/2, y_center=h/2)
    return cropped_clip