import PyPDF2
import pyttsx3

try:
    pdfReader = PyPDF2.PdfReader(open('dummypdf.pdf', 'rb'))

    # Initialize the Pyttsx3 engine
    speaker = pyttsx3.init()

    # Initialize the 'text' variable to accumulate text from all pages
    text = ""

    for page_num in range(len(pdfReader.pages)):
        page = pdfReader.pages[page_num]
        text += page.extract_text()
        speaker.say(page.extract_text())
        speaker.runAndWait()
    speaker.stop()

    # Save the accumulated text to an audio file
    speaker.save_to_file(text, 'audio.mp3')
    speaker.runAndWait()

except Exception as e:
    print("An error occurred:", str(e))
