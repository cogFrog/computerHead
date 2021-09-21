import os

while(True):
	text = "espeak \"" + input() + "\" -a 200 --stdout | aplay -D \'default\'"
	#print(text)
	os.system(text)
	# replicating sample command: espeak "how are you today?" --stdout | aplay -D 'default'
