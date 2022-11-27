"""
User chooses a factor to adjust the speed of the subtitles by.
"""

import pysrt

if __name__ == "__main__":

    srt_file_path = input("Enter the path of the subtitles file: ")
    factor = float(input("Enter the factor to adjust the subtitles by: "))

    subs = pysrt.open(srt_file_path)

    subs.shift(ratio = factor)

    subs.save('output/adjusted.srt', encoding='utf-8')