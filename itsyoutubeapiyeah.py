
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
vid_id = 'Xh2TY0DMbas'
data = yta.get_transcript(vid_id)
transcript = ''
for value in data:
    for key,val in value.items():
        if key == 'text':
            transcript += val
            
l = transcript.splitlines()
final_tran = " ".join(l)

file = open("youtube.txt", 'w')
file.write(final_tran)
file.close()


