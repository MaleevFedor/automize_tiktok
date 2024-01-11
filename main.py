from renderer import render
from moviepy.config import change_settings
from datetime import datetime




if __name__ == '__main__':
    startTime = datetime.now()
    change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})
    render('files/funny).mp4').write_videofile('result.mp4', fps=30)
    print(datetime.now() - startTime)
    #ToDo return 60 fps


