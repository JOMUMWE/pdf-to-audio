from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .logic.pdf_text import extract_text_from_pdf_convert_to_audio
import asyncio


# Create your views here.

def index(request):
    template = loader.get_template("app/index.html")
    return HttpResponse(template.render())

def reader(request):
    # text = asyncio.run(extract_text_from_pdf_convert_to_audio("./test.pdf"))
    # mydict = {
    #     "text":text,
    #     "audio": './logic/output.mp3'
    # }
    template = loader.get_template("app/reading.html")
    return HttpResponse(template.render())