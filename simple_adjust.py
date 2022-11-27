import pysrt
from moviepy.editor import VideoFileClip
from datetime import datetime

def get_video_duration(filename):
    clip = VideoFileClip(filename)
    duration = clip.duration

    return duration

def get_subs_duration(subs):
    t = subs[-1].end.to_time()
    
    # convert to seconds
    duration = (t.hour * 60 + t.minute) * 60 + t.second

    return duration


if __name__ == "__main__":
    srt_file_path = input("Enter the path of the subtitles file: ")
    video_file_path = input("Enter the path of the video file: ")

    subs = pysrt.open(srt_file_path)

    subs_duration = get_subs_duration(srt_file_path)
    video_duration = get_video_duration(video_file_path)

    ratio = video_duration / subs_duration

    subs.shift(ratio = ratio)

    subs.save('adjusted.srt', encoding='utf-8')

# TODO : test and document