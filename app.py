from fastapi import FastAPI, File, UploadFile
import pytesseract
import cv2
import shutil
import os
from PIL import Image
from pdf2image import convert_from_path

app = FastAPI()


POPPLER_PATH = r"C:\Program Files\poppler-24.08.0\Library\bin"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\\tesseract.exe"

@app.post("/extract-id/")
async def extract_id(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = ""

    if file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):  
        image = cv2.imread(file_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        extracted_text = pytesseract.image_to_string(gray)

    elif file.filename.lower().endswith('.pdf'):  
        images = convert_from_path(file_path, poppler_path=POPPLER_PATH)
        for img in images:
            text = pytesseract.image_to_string(img)
            extracted_text += text + "\n"

    os.remove(file_path)

    return {"status": "success", "extracted_text": extracted_text}