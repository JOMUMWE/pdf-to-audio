from pypdf import PdfReader
from gtts import gTTS
from googletrans import Translator
import asyncio


async def extract_text_from_pdf_convert_to_audio(pdf_file):
    text = ''
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    audio = gTTS(text=text,lang='en',slow=False)
    await audio.save('output.mp3')
    return text
    




