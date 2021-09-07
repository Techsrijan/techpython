from gtts import gTTS
text="Hello how are you? I am fine thank you."
a=gTTS(text)
a.save('train.mp3')