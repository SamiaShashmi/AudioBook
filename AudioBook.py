import pyttsx3
import PyPDF2

book = open('Policy of IUT.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
friend = pyttsx3.init()
for x in range(0, pages):
    page = pdfReader.getPage(x)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()