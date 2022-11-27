"""
The user needs to check the timestamps for when the video file has the last line of the film's dialogue and to remove substitle credits.

Dont do this if you dont want to risk any spoliers!
"""

import pysrt

def get_subs_duration(subs):
    """
    Get subtitles duration in seconds
    """
    t = subs[-1].end.to_time()
    
    # convert to seconds
    duration = (t.hour * 60 + t.minute) * 60 + t.second

    return duration


def parse_time(time):
    """
    Parse time in format hh:mm:ss and convert to seconds
    """
    t = time.split(':')
    h = int(t[0])
    m = int(t[1])
    s = int(t[2])

    duration = (h * 60 + m) * 60 + s

    return duration


if __name__ == "__main__":

    srt_file_path = input("Remove the credits from the subtitles file. Enter the path of the subtitles file: ")
    video_ending = input("Enter the time of the last line of the film's dialogue (hh:mm:ss): ")

    subs = pysrt.open(srt_file_path)

    subs_duration = get_subs_duration(subs)
    video_duration = parse_time(video_ending)

    # get the ratio between video and subs
    ratio = video_duration / subs_duration

    subs.shift(ratio = ratio)

    subs.save('output/adjusted.srt', encoding='utf-8')
