# Product Requirements Document

## OCR Text Scanner

**Version:** 2.0  
**Status:** Simple MVP  
**Primary UI:** Streamlit  
**Target user:** Beginner / non-technical user

## 1. Product Summary

Build a small Python application that lets a user upload an image, extract printed text from it using OCR, view a simple image description, edit the extracted text, and download it.

The application must be easy to run, easy to explain in an interview, and easy to improve later.

## 2. Problem

Text inside screenshots, receipts, posters, photographs, and scanned pages is difficult to edit or reuse. The application converts that image text into editable digital text.

## 3. Goals

- Provide a simple Streamlit interface.
- Support one image at a time.
- Extract English printed text locally.
- Show the uploaded image before scanning.
- Show extracted text in an editable area.
- Show a separate simple image description.
- Allow the user to download the text.
- Handle common invalid-image and OCR errors clearly.
- Keep the project structure small enough for a beginner to understand.

## 4. Users and Use Cases

| User | Use case |
|---|---|
| General user | Upload an image and obtain editable text. |
| Student or beginner developer | Understand and explain a complete OCR application. |
| Tester | Use sample images to check successful and failed OCR cases. |

## 5. MVP Scope

### In Scope

- PNG, JPG, and JPEG uploads.
- Maximum upload size of 10 MB.
- Image preview.
- Explicit **Scan Text** button.
- Local RapidOCR text extraction.
- English printed text support by default.
- Editable extracted text.
- TXT download.
- Simple image description based on image size, orientation, and OCR result.
- Reset and new-image workflow.
- Friendly validation and error messages.
- Local execution through Streamlit.
- One smoke test for application startup.

### Out of Scope

- PDF and multi-page documents.
- Batch processing.
- User login or database storage.
- Cloud OCR APIs.
- Handwriting recognition guarantees.
- Object-level image understanding.
- Bounding boxes or advanced document editing.
- Custom frontend HTML, CSS, JavaScript, or Flask backend.

## 6. User Journey

1. User runs the Streamlit application.
2. User uploads a JPG, JPEG, or PNG image.
3. The application validates and previews the image.
4. User clicks **Scan Text**.
5. RapidOCR extracts readable text locally.
6. The application displays the text and a simple image description.
7. User reviews or edits the text.
8. User downloads the text or selects **Reset**.

## 7. Functional Requirements

| ID | Requirement | Acceptance condition |
|---|---|---|
| FR-001 | Application launch | `streamlit run app.py` opens the application. |
| FR-002 | Upload | User can choose PNG, JPG, or JPEG files. |
| FR-003 | Validation | Empty, corrupt, unsupported, and oversized files show a friendly error. |
| FR-004 | Preview | A valid uploaded image is displayed before OCR. |
| FR-005 | Explicit scan | OCR runs only after the user clicks **Scan Text**. |
| FR-006 | Processing feedback | A spinner or status message appears while OCR runs. |
| FR-007 | Extracted text | Recognized text appears in an editable text area. |
| FR-008 | Image description | A separate description reports orientation, dimensions, and text detection status. |
| FR-009 | Empty result | No-text images show a clear warning. |
| FR-010 | Download | The displayed text can be downloaded as UTF-8 TXT. |
| FR-011 | Reset | Reset clears the current result. |
| FR-012 | New image | Selecting another image clears the previous result. |

## 8. User Interface Requirements

Use Streamlit fundamentals only:

- `st.set_page_config()` for page setup.
- `st.file_uploader()` for image selection.
- `st.image()` for preview.
- `st.button()` for Scan Text and Reset.
- `st.spinner()` for processing feedback.
- `st.text_area()` for editable output.
- `st.download_button()` for TXT export.
- `st.info()`, `st.warning()`, and `st.error()` for clear messages.
- `st.session_state` only for the current scan result and selected-file tracking.

## 9. Technology and Dependencies

- Python 3.10 or newer.
- Streamlit for the user interface.
- Pillow for image loading and validation.
- RapidOCR ONNX Runtime for local OCR.
- Pytest for the startup test.
- Ruff for code-quality checks.

The complete dependency list is in `requirements.txt`.

## 10. Simple Project Structure

```text
OCR_Image_Scanner/
├── app.py                 # Streamlit user interface
├── ocr_logic.py           # Image validation, OCR, and description logic
├── requirements.txt       # Python dependencies
├── README.md              # Setup and interview guide
├── tests/
│   └── test_app.py        # Application startup test
└── sample_data/           # Example images
```

The MVP intentionally uses only two application files so a beginner can understand the full workflow without a large folder structure. `app.py` is the UI layer and `ocr_logic.py` is the business-logic layer.

## 11. Privacy and Security

- Process images locally.
- Do not send images to external services.
- Do not permanently store uploaded images.
- Do not add credentials or API keys to the project.
- Do not expose internal exception details to normal users.

## 12. Testing Requirements

Minimum test coverage:

- Application starts without Streamlit errors.
- Sample image OCR returns text.
- Invalid, empty, corrupt, and oversized images are handled during manual verification.
- Reset and new-image behavior are manually checked.

Validation commands:

```powershell
pytest
ruff check .
streamlit run app.py
```

## 13. MVP Definition of Done

- Streamlit application launches successfully.
- User can upload and preview a supported image.
- Scan Text explicitly starts OCR.
- Extracted text is displayed and editable.
- Image description is displayed separately.
- Text downloads as TXT.
- Reset and new-image behavior do not show stale results.
- Invalid images and OCR failures are handled clearly.
- README explains setup and interview concepts.
- Tests and Ruff checks pass.

## 14. Future Roadmap

- Multilingual OCR.
- PDF and multi-page support.
- Batch image processing.
- OCR confidence scores.
- Bounding boxes.
- Better object-level image descriptions using a vision model.
- Cloud deployment.

Future features must not be added until the MVP definition of done passes.

## 15. Instruction to Anti-Gravity

Implement only the simple Streamlit MVP described here. Prefer readable Python over complex architecture. Keep the project structure small. At the end of each phase, list changes, run checks, and explain the result in beginner-friendly language.

See [OCR_Image_to_Text_Implementation_Plan.md](OCR_Image_to_Text_Implementation_Plan.md) for the phase-wise implementation plan.
