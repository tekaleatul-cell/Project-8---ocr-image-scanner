# OCR Text Scanner

A beginner-friendly Streamlit application that reads text from an uploaded image.

## Simple Project Structure

Only these six items are needed to run the application:

- `app.py`
- `ocr_logic.py`
- `requirements.txt`
- `README.md`
- `run_app.bat` (one-click launcher)
- `runtime.txt` (Streamlit Cloud Python version)
- `sample_data/` (optional examples)

The test and planning files are supporting material, not part of the application flow. The `.venv` folder is a local Python environment and is hidden from the VS Code Explorer.

```text
OCR_Image_Scanner/
├── app.py                 # The complete Streamlit application
├── ocr_logic.py           # Image validation, OCR, and description logic
├── requirements.txt       # Python packages needed to run it
├── README.md              # Setup and interview explanation
├── run_app.bat             # Simple application launcher
├── runtime.txt              # Uses Python 3.12 in Streamlit Cloud
├── tests/
│   └── test_app.py        # Simple startup test
└── sample_data/           # Example images for testing
```

The project uses two code files: `app.py` handles the interface, and `ocr_logic.py` handles the business logic. This keeps the structure small while making the design easy to explain.

## UI and Business Logic

- `app.py`: Streamlit page, upload control, buttons, preview, messages, and download.
- `ocr_logic.py`: Image validation, RapidOCR execution, result statistics, and image description.

## Features

- Upload a JPG, JPEG, or PNG image.
- Preview the image.
- Click **Scan Text** to run local OCR.
- Review and edit extracted text.
- Download the result as a `.txt` file.
- See a simple image description.
- Handle empty, invalid, corrupt, and oversized images.
- Reset when selecting a different image.

## Technology

- **Python:** Application language.
- **Streamlit:** Creates the web interface without separate HTML or JavaScript.
- **Pillow:** Opens and validates uploaded images.
- **RapidOCR:** Recognizes printed text locally.

## Run on Windows

### First time only

Open PowerShell in this project folder and run these commands one by one:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Every other time

Double-click `run_app.bat` or open PowerShell in the project folder and run:

```powershell
.\run_app.bat
```

Then open the link shown in the terminal, usually http://localhost:8501.

To stop the application, press `Ctrl+C` in the terminal.

## Test and Lint

```powershell
pytest
ruff check .
```

## How to Explain It in an Interview

**Question: What does the application do?**  
It accepts an image, sends it to an OCR model, displays the recognized text, and lets the user download it.

**Question: Why did you use Streamlit?**  
I used Streamlit because it provides upload controls, buttons, image previews, text areas, and download buttons with very little frontend code. It is a good choice for a small Python-focused MVP.

**Question: What happens when a user scans an image?**

1. Streamlit receives the uploaded file.
2. Pillow checks that it is a valid image and is below 10 MB.
3. RapidOCR reads the text from the image.
4. The result is stored in Streamlit session state.
5. The text and image description are displayed.
6. The user can edit and download the text.

**Question: Why is the OCR model cached?**  
OCR model loading is expensive. `st.cache_resource` loads RapidOCR once and reuses it, so the model does not reload on every Streamlit interaction.

**Question: How are errors handled?**  
The app checks for empty, corrupt, unsupported, and oversized files. OCR failures show a friendly message instead of crashing the application.

**Question: What are future improvements?**  
A future version could add multilingual OCR, PDF support, batch processing, confidence scores, and a dedicated image-understanding model for richer descriptions.

## Privacy and MVP Limits

Images are processed locally. The MVP supports one image at a time and is intended for printed text. The current description reports orientation, size, and whether text was detected; it does not identify objects such as receipts or handwritten notes.

The product requirements remain in [OCR_Image_to_Text_PRD_AntiGravity.md](OCR_Image_to_Text_PRD_AntiGravity.md), and the detailed plan remains in [OCR_Image_to_Text_Implementation_Plan.md](OCR_Image_to_Text_Implementation_Plan.md).

## Deploy on Streamlit Cloud

The repository includes `runtime.txt` to use Python 3.12. This avoids the OpenCV import problem that can occur with Python 3.14 and RapidOCR.

After adding or changing deployment files:

```powershell
git add .
git commit -m "Fix Streamlit Cloud Python version"
git push
```

In Streamlit Cloud, open **Manage app**, then select **Reboot app** or **Redeploy**. Set the main file to `app.py` and wait for dependencies to reinstall.
