import pyttsx3
import PyPDF2
from PyPDF2 import PdfFileReader
import sys
import json
from pygments import highlight, lexers, formatters

path = '/Users/manasdash/Desktop/97_Things_Every_Programmer_Should_Know.pdf'
# pdf_reader = PyPDF2.PdfFileReader(book)
# pages = pdf_reader.numPages
#
# print(pages)
#
# speaker = pyttsx3.init()
# page = pdf_reader.getPage(1)
# text = page.extractText()
# print(text)
# speaker.say(text)
# speaker.runAndWait()
#
# # get_doc_info.py
#



def get_info(path):
	with open(path, 'rb') as f:
		pdf = PdfFileReader(f)
		info = pdf.getDocumentInfo()
		number_of_pages = pdf.getNumPages()

	author = info.author
	creator = info.creator
	producer = info.producer
	subject = info.subject
	title = info.title

	formatted_json = json.dumps(info, indent=4)
	print(formatted_json)

if __name__ == '__main__':

	get_info(path)