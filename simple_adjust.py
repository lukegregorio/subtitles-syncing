"""
Adjust the subtitle speed assuming that the end of the subtitles 'match' the end of the video file
"""

import pysrt
from moviepy.editor import VideoFileClip
from datetime import datetime

def get_video_duration(filename):
    """
    Get video duration in seconds
    """
    clip = VideoFileClip(filename)
    duration = clip.duration

    return duration

def get_subs_duration(subs):
    """
    Get subtitles duration in seconds
    """
    t = subs[-1].end.to_time()
    
    # convert to seconds
    duration = (t.hour * 60 + t.minute) * 60 + t.second

    return duration


if __name__ == "__main__":

    srt_file_path = input("Enter the path of the subtitles file: ")
    video_file_path = input("Enter the path of the video file: ")

    subs = pysrt.open(srt_file_path)

    subs_duration = get_subs_duration(subs)
    video_duration = get_video_duration(video_file_path)
    
    # get the ratio between video and subtitles duration which is used to adjust the subtitles timings - assumes the 'endings' of both files are the same
    ratio = video_duration / subs_duration

    subs.shift(ratio = ratio)

    subs.save('output/adjusted.srt', encoding='utf-8')