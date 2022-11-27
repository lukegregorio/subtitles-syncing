"""
WIP . Use video audio detection to detect when the video file last line of the movie is delivered.
"""

import pysrt
import moviepy.editor as mp


srt_file_path = input("Enter the path of the subtitles file: ")
video_file_path = input("Enter the path of the video file: ")
# video_end = input("Enter the rough end time of the video in minutes: ") - or i just use the duration of the video and get x mins before then
hf_access_token = input("Enter the access token for the HF API from https://huggingface.co/settings/tokens: ")


subs = pysrt.open(srt_file_path)

subs_start = subs[0].start
# i manually trim the end of the subtitles to remove credits - not sure for now if this can be automated
subs_end = subs[-1].end

# read in video as audio
clip = mp.VideoFileClip(video_file_path).subclip(-600) # trim the last 10 mins of the video - might be better to build in some logic which reads in video until it hits voice
clip.audio.write_audiofile("film_audio.mp3")

from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained("pyannote/voice-activity-detection",
                                    use_auth_token=hf_access_token)

output = pipeline("film_audio.mp3")

# prints out graph of audio with voice activity
output.get_timeline().support()


# you can adjust the speed by using the ratio arg of the shift method
subs.shift(ratio = 0.5) # half the speed
subs.shift(ratio = 2) # double the speed
