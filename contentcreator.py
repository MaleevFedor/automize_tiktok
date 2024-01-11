from moviepy.video.VideoClip import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video import fx
import whisper_timestamped


def prepare_content(clip, res=(1920, 1080)):
    clip.audio.write_audiofile('sound.mp3')
    model = whisper_timestamped.load_model('base')
    file = 'sound.mp3'
    result = whisper_timestamped.transcribe(model, file)

    generator = lambda txt: TextClip(txt, font='fonts/BurbankBig.oft',
                                     fontsize=110, color='white',
                                     stroke_color='black', stroke_width=7)
    subs = []
    for segment in result["segments"]:
        for word in segment["words"]:
            text = word["text"].upper().replace(',', '')
            start = word["start"]
            end = word["end"]
            subs.append(((start, end), text))
    subtitles = SubtitlesClip(subs, generator)
    #clip = clip.resize(2)
    (w, h) = clip.size
    # ToDo work with every resolution
    cropped_clip = fx.all.crop(clip, width=1080, height=960, x_center=w / 2, y_center=h / 2)
    return (cropped_clip, subtitles)
