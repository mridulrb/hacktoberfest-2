import pyttsx3
from typing import Text
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('Your PDF file ', 'rb'))

speaker = spyttsx3.init()

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

speaker.save_to_file(text, 'audio.mp3')
speaker.runAndWait()
