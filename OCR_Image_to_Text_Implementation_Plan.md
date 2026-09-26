# OCR Text Scanner Implementation Plan

**Application:** Simple Streamlit OCR MVP  
**Source PRD:** [OCR_Image_to_Text_PRD_AntiGravity.md](OCR_Image_to_Text_PRD_AntiGravity.md)

## Implementation Principle

Build the smallest useful application first. Use two application files: `app.py` for the Streamlit UI and `ocr_logic.py` for business logic. Avoid additional folders unless the project grows.

## Phase 0: Confirm Requirements

**Goal:** Agree on the MVP before coding.

- Confirm Streamlit as the UI framework.
- Confirm PNG, JPG, and JPEG support.
- Confirm one image at a time and a 10 MB limit.
- Confirm local RapidOCR and no cloud service.
- Confirm the MVP acceptance checklist.

**Exit check:** No product decision is blocking development.

## Phase 1: Create the Simple Project

**Goal:** Create the minimum files.

```text
app.py
ocr_logic.py
requirements.txt
README.md
tests/test_app.py
sample_data/
```

Tasks:

- Create a Python virtual environment.
- Add Streamlit, Pillow, RapidOCR, Pytest, and Ruff to `requirements.txt`.
- Create a basic Streamlit page in `app.py`.
- Create `ocr_logic.py` for image validation, OCR, and description functions.
- Add setup and interview explanations to `README.md`.

**Exit check:** `streamlit run app.py` opens without an error.

## Phase 2: Add Upload and Validation

**Goal:** Receive a safe, readable image.

Tasks:

- Add `st.file_uploader()`.
- Allow only PNG, JPG, and JPEG.
- Reject empty files.
- Reject files larger than 10 MB.
- Use Pillow to confirm the file is a real image.
- Display the image with `st.image()`.

**Exit check:** A valid sample image previews, and invalid files show a friendly message.

## Phase 3: Add OCR

**Goal:** Extract text from the image.

Tasks:

- Load RapidOCR with `st.cache_resource`.
- Run OCR only after the user clicks **Scan Text**.
- Convert OCR output into plain text lines.
- Show `st.spinner()` during scanning.
- Handle no text and OCR errors with clear messages.

**Exit check:** The sample text image produces readable text.

## Phase 4: Add Results

**Goal:** Make the result useful to the user.

Tasks:

- Show the extracted text in `st.text_area()`.
- Allow the user to edit the text.
- Add `st.download_button()` for a TXT file.
- Add the simple local image description.
- Display word count, character count, and processing time.

**Exit check:** The user can review, edit, and download the text.

## Phase 5: Add Reset and State Handling

**Goal:** Prevent old results from appearing for a new image.

Tasks:

- Store the current result in `st.session_state`.
- Track the selected file name and size.
- Clear the result when a new image is selected.
- Add a **Reset** button.

**Exit check:** Reset and new-image selection produce a clean workflow.

## Phase 6: Test and Explain

**Goal:** Confirm the MVP works and is easy to present.

Run:

```powershell
pytest
ruff check .
streamlit run app.py
```

Manually check:

- Valid text image.
- Blank image.
- Corrupt image.
- Unsupported file.
- Oversized file.
- New image after an earlier scan.
- Reset button.
- TXT download.

**Exit check:** Tests and Ruff pass, and all MVP acceptance criteria are demonstrated.

## Phase 7: Documentation and Handoff

**Goal:** Make the project understandable to a new beginner.

Update `README.md` with:

- What the application does.
- Why Streamlit was selected.
- What each dependency does.
- How the upload-to-OCR flow works.
- How to run, test, and lint the project.
- How to explain the project in an interview.
- Current limitations and future improvements.

## Interview Explanation

Use this short explanation:

> This is a Streamlit OCR application. The user uploads an image, Pillow validates and opens it, RapidOCR extracts the printed text, and Streamlit displays the result. The user can edit and download the text. I used `st.cache_resource` so the OCR model loads once instead of on every interaction. I separated the UI in `app.py` from the business logic in `ocr_logic.py` while keeping the project small.

## Final Definition of Done

- `app.py` contains the Streamlit UI.
- `ocr_logic.py` contains the business logic.
- The application runs with `streamlit run app.py`.
- Upload, preview, scan, result, description, download, and reset work.
- Invalid and no-text cases are understandable.
- `pytest` passes.
- `ruff check .` passes.
- README setup and interview guidance are complete.
