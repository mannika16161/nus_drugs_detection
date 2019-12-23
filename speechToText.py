import speech_recognition as sr

r = sr.Recognizer()
demo = sr.AudioFile('demo.wav')
dict={}
with demo as source:
	audio = r.record(source)
	print(type(audio))
	get = r.recognize_google(audio)
	if get in dict:
		print(get)
