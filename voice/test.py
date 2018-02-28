import cv2
import numpy as np
import os
import speech_recognition as sr
import threading
import pyttsx3
import sys
import multiprocessing
def movement():
	gpio=1

def voice():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)

		# recognize speech using Sphinx
	try:
		print("Google thinks you said " + r.recognize_google(audio))
	except sr.UnknownValueError:
		print("Google could not understand audio")
	except sr.RequestError as e:
		print("Google error; {0}".format(e))

def mainvoice():
	r=sr.Recognizer()
	engine=pyttsx3.init()
	#rate=engine.getProperty("rate")
	#engine.setProperty('rate',rate+50)
	with sr.Microphone() as source:
		count=3;
		while(1):
			engine.say("say the password")
			engine.runAndWait()
			print("speak something")
			try:
				passaudio=r.listen(source)
				password=r.recognize_google(passaudio)


				if "Ganesh" in password:

					print("entered into the system")
					engine.say("enter Master")
					while(1):
						print("speak")
						audio=r.listen(source)


						try:
							word=r.recognize_google(audio)
							print(word)
							if 'video' in word:
								processid=os.fork()
								if processid==0:
									video()
									sys.exit()
								else:
									lol=1
							if 'voice' in word:
								voice()
							if 'exit' in word:
								sys.exit()

						except sr.UnknownValueError:
							print("google cant understand")
						except sr.RequestError as e:
							print("Google error; {0}".format(e))
				else:
					engine.say("you identity is wrong,you have"+str(count)+"remaining")
					count=count-1;
					if(count==-1):
						sys.exit()
			except sr.UnknownValueError:
				print("google cant understand")
			except sr.RequestError as e:
				print("Google error; {0}".format(e))

	return 1;



def video():
	camera=cv2.VideoCapture(0)  #created video object
	while(camera.isOpened()):
		ret,frame=camera.read()
		cv2.imshow('frame',frame)
		grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		cv2.imshow("grayframe",grayframe)
		if(cv2.waitKey(2) & 0xFF == ord('q')):
			break
	camera.release()
	cv2.destroyAllWindows()
def main():
	mainvoice()






if (__name__=='__main__'):
	main()
