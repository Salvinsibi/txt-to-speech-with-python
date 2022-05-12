# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'hello my name is salvin.'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=>

# Saving the converted audio in a mp3 file nam>
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 txtspeech.mp3")
#@salvin sibi
