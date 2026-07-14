from youtube_transcript_api import YouTubeTranscriptApi

video_id = "rfscVS0vtbw"

try:
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print(transcript)

except Exception as e:
    print("Transcript not available for this video")
    print("Error:", e)