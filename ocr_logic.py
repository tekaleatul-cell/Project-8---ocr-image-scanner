"""Business logic for the simple OCR application."""

from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO

from PIL import Image, UnidentifiedImageError

MAX_FILE_SIZE = 10 * 1024 * 1024


@dataclass
class ScanResult:
    """Text and basic information returned by OCR."""

    text: str
    engine: str
    processing_time_ms: float

    @property
    def word_count(self) -> int:
        return len(self.text.split())

    @property
    def character_count(self) -> int:
        return len(self.text)


def load_ocr_model():
    """Load RapidOCR when the application asks for it."""
    from rapidocr_onnxruntime import RapidOCR

    return RapidOCR()


def read_uploaded_image(uploaded_file) -> Image.Image:
    """Validate the upload and return a Pillow image."""
    if uploaded_file.size == 0:
        raise ValueError("The uploaded file is empty.")
    if uploaded_file.size > MAX_FILE_SIZE:
        raise ValueError("The image must be smaller than 10 MB.")

    try:
        image = Image.open(BytesIO(uploaded_file.getvalue()))
        image.load()
        return image.convert("RGB")
    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError("The uploaded file is not a valid image.") from exc


def scan_text(image: Image.Image, ocr_model) -> ScanResult:
    """Run OCR and convert detected lines into plain text."""
    import time

    start = time.perf_counter()
    raw_result, _timing = ocr_model(image)
    lines = [item[1] for item in raw_result or [] if len(item) > 1 and item[1]]
    return ScanResult(
        text="\n".join(lines),
        engine="RapidOCR",
        processing_time_ms=(time.perf_counter() - start) * 1000,
    )


def describe_image(image: Image.Image, result: ScanResult) -> str:
    """Create a simple local description from image metadata and OCR status."""
    width, height = image.size
    ratio = width / height if height else 1
    orientation = "landscape" if ratio > 1.25 else "portrait" if ratio < 0.8 else "square"
    text_status = "Readable text was detected." if result.text.strip() else "No readable text was detected."
    return f"This is a {orientation} image measuring {width} x {height} pixels. {text_status}"
