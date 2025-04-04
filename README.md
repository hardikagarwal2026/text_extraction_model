# Text Extraction Model

## Overview
This project provides a FastAPI-based text extraction service that utilizes Tesseract OCR and Poppler to extract text from images and PDF files. It allows users to upload files via API endpoints and receive extracted text in response.

## Features
- Supports image-based text extraction using Tesseract OCR
- Supports PDF text extraction using Poppler
- RESTful API built with FastAPI
- Asynchronous file handling for efficient processing

## Requirements
Ensure you have the following installed before running the application:
- Python 3.8+
- FastAPI
- pytesseract
- OpenCV
- Pillow
- pdf2image
- Poppler

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/hardikagarwal2026/text_extraction_model.git
   cd text_extraction_model
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Setup
Ensure Tesseract OCR and Poppler are installed on your system:
- **Tesseract OCR**: Download and install from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- **Poppler**: Install from [Poppler for Windows](https://blog.alivate.com.au/poppler-windows/) or use `apt-get install poppler-utils` on Linux.

Modify the paths in `app.py` if necessary:
```python
POPPLER_PATH = r"C:\Program Files\poppler-24.08.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Usage
1. Start the FastAPI server:
   ```sh
   uvicorn app:app --reload
   ```
2. Open the API docs in your browser:
   - Go to: `http://127.0.0.1:8000/docs`

## API Endpoints
### 1. Extract Text from an Image or PDF
- **Endpoint:** `POST /extract-id/`
- **Request:** Upload a file (image or PDF)
- **Response:** Extracted text

**Example cURL request:**
```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/extract-id/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@sample.pdf'
```

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contributors
- **Hardik Agarwal**

## Acknowledgments
- Tesseract OCR
- FastAPI
- Poppler
