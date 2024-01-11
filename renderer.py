from moviepy.editor import *
from gameplay import prepare_gameplay
from contentcreator import prepare_content
import moviepy.editor as mpy
import multiprocessing


def render(path):
    clip = mpy.VideoFileClip(path)
    duration = int(clip.duration)
    res = tuple(clip.size)
    #ToDO multiprocessing
    #ToDo subtitles function
    gameplay = prepare_gameplay(duration, res).subclip(0, 0 + duration)
    content = prepare_content(clip, res)
    content, subtitles = content
    content = content.subclip(0, 0 + duration)
    result = clips_array([[content],
                          [gameplay]])
    result = CompositeVideoClip([result, subtitles.set_position(('center', int(res[0]*0.54)))])
    #x y
    #ToDo scayling subtitles for different resolutions
    return result