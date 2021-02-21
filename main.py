from youtube_transcript_api import YouTubeTranscriptApi
import sys
import os


#
# if __name__ == "__main__":
#     print(f"Arguments count: {len(sys.argv)}")
#     for i, arg in enumerate(sys.argv):
#         print (f"Argument {i:>6}: {arg}")


t = YouTubeTranscriptApi.get_transcript(video_id="na0g_DsNXr8")


def toJSON(youtube_id):
    return YouTubeTranscriptApi.get_transcript(video_id=youtube_id)

