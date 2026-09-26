"""Streamlit user interface for the OCR Text Scanner."""

from __future__ import annotations

import sys

import streamlit as st

from ocr_logic import (
    ScanResult,
    describe_image,
    load_ocr_model,
    read_uploaded_image,
    scan_text,
)


@st.cache_resource
def get_ocr_model():
    """Cache the OCR model so it is loaded only once."""
    return load_ocr_model()


def main() -> None:
    st.set_page_config(page_title="OCR Text Scanner", page_icon="🔎", layout="wide")

    if sys.version_info[:2] != (3, 12):
        st.error(
            "This deployment requires Python 3.12. "
            f"The current environment is Python {sys.version_info.major}.{sys.version_info.minor}. "
            "Update runtime.txt and redeploy the app."
        )
        st.stop()

    st.title("OCR Text Scanner")
    st.write("Upload an image, scan its text locally, and download the result.")

    uploaded_file = st.file_uploader(
        "Choose a JPG, JPEG, or PNG image",
        type=["jpg", "jpeg", "png"],
        help="Maximum file size: 10 MB.",
    )

    if uploaded_file is None:
        st.info("Upload an image to begin.")
        return

    try:
        image = read_uploaded_image(uploaded_file)
    except ValueError as error:
        st.error(str(error))
        return

    file_key = f"{uploaded_file.name}:{uploaded_file.size}"
    if st.session_state.get("file_key") != file_key:
        st.session_state.file_key = file_key
        st.session_state.pop("scan_result", None)

    preview_col, result_col = st.columns(2)
    with preview_col:
        st.subheader("Uploaded image")
        st.image(image, use_container_width=True)
        st.caption(f"{uploaded_file.name} · {image.width} x {image.height} pixels")

        scan_col, reset_col = st.columns(2)
        with scan_col:
            scan_clicked = st.button("Scan Text", type="primary", use_container_width=True)
        with reset_col:
            reset_clicked = st.button("Reset", use_container_width=True)

        if reset_clicked:
            st.session_state.pop("scan_result", None)
            st.session_state.pop("file_key", None)
            st.rerun()

        if scan_clicked:
            with st.spinner("Scanning image..."):
                try:
                    st.session_state.scan_result = scan_text(image, get_ocr_model())
                except (OSError, RuntimeError, ValueError):
                    st.error("The OCR engine could not process this image.")

    with result_col:
        st.subheader("Image description")
        result: ScanResult | None = st.session_state.get("scan_result")
        if result is None:
            st.caption("The description will appear after scanning.")
        else:
            st.write(describe_image(image, result))

        st.subheader("Extracted text")
        if result is None:
            st.caption("Select Scan Text to extract the image text.")
        elif not result.text.strip():
            st.warning("No readable text was detected in this image.")
        else:
            edited_text = st.text_area("Review and edit", value=result.text, height=260)
            st.download_button(
                "Download TXT",
                data=edited_text.encode("utf-8"),
                file_name="extracted-text.txt",
                mime="text/plain",
                use_container_width=True,
            )
            st.caption(
                f"{result.word_count} words · {result.character_count} characters · "
                f"{result.processing_time_ms:.0f} ms"
            )


if __name__ == "__main__":
    main()
