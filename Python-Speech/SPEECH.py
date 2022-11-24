#yPDF2 is a free and open-source pure-python 
# pip install PyPDF2
# PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files


#pyttsx3 is a text-to-speech conversion library in Python


#pip install pyttsx3


import PyPDF2

import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open('dummypdf.pdf', 'rb'))

#######CASE 1 PDF READ
# Initialize the Pyttsx3 engine

speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()



speaker.save_to_file(text, 'audio.mp3')


 
####CASE 2 READ A STRING ###########
# Create a string
string = "Lorem Ipsum is simply dummy text " \
    + "of the printing and typesetting industry."
 
# Initialize the Pyttsx3 engine
engine = pyttsx3.init()
 
# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'speech.mp3')
 
# Wait until above command is not finished.
engine.runAndWait()


