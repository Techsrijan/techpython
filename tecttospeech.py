from gtts import gTTS
from playsound import playsound
text="Hello how are you? I am fine thank you."
a=gTTS(text)
a.save('train.mp3')
playsound('train.mp3')