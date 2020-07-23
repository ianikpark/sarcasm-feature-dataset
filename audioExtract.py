# from converter import converter
# import os

# c = Converter()

# directory = os.fsencode("input/non-sarcastic")

# for file in os.listdir(directory):
#      filename = os.fsdecode(file)
#      if filename.endswith(".mp4"): 
#         clip = filename
#         conv = c.convert(clip, 'audio.mp3', {'format':'mp3','audio':{'codec': 'mp3','bitrate':'22050','channels':1}})
#         for timecode in conv:
#         	pass

#         audioFile = filename
#     	os.system("mpg123 -w audio.wav audio.mp3")
#          continue
#      else:
#          continue


import os
import subprocess

inputdir = 'output/merged/'
outputdir = 'output/audio/'

all_files = os.listdir(inputdir)

if(not os.path.isdir(outputdir)):
	os.mkdir(outputdir)

for f in all_files:
	command = "ffmpeg -i " + inputdir + f + " -ab 160k -ac 2 -ar 44100 -vn " + outputdir + f.split('.')[0] + ".wav"
	subprocess.call(command, shell=True)