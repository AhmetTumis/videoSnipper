import os
#os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

import moviepy.editor as mp
import ffmpeg

sample_clip = mp.VideoFileClip(r"vid/sample_video.mp4")

print(type(sample_clip))

sample_clip.audio.write_audiofile(r"audio/audio_from_sample_clip.mp3")