from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from utils import batch_to_binary, binary_to_bits
import pdfplumber

FONT_NAME = "Helvetica"
FONT_SIZE = 12
LEFT_MARGIN = 70
NORMAL_SPACE = 8      # points
DELTA_MM = 0.4   # Use 3 for testing first
DELTA = DELTA_MM * mm

def draw_sentence(c, sentence, x, y, bit):
    """
    Draw each word individually.
    If bit == 1, widen only the FIRST gap.
    """

    words = sentence.split()

    current_x = x

    for i, word in enumerate(words):

        c.drawString(current_x, y, word)

        current_x += c.stringWidth(word, FONT_NAME, FONT_SIZE)

        space = NORMAL_SPACE

        # Only modify the FIRST gap
        if i == 0 and bit == 1:
            space += DELTA

        current_x += space


def embed_watermark(input_pdf_path, batch_id, output_pdf_path):

    c = canvas.Canvas(output_pdf_path, pagesize=A4)

    width, height = A4

    c.setFont(FONT_NAME, FONT_SIZE)

    sentences = extract_lines(input_pdf_path)

    y = height - 100

    binary = batch_to_binary(batch_id)

    bits = binary_to_bits(binary)

    bit_index = 0

    for sentence in sentences:

        draw_sentence(c, sentence, LEFT_MARGIN, y, bits[bit_index])

        y -= 30

        bit_index = (bit_index + 1) % len(bits)

        if y < 60:

            c.showPage()

            c.setFont(FONT_NAME, FONT_SIZE)

            y = height - 60

    c.save()

    print("PDF Generated Successfully!")

def extract_lines(pdf_path):

    all_lines = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:

                all_lines.extend(
                    line.strip()
                    for line in text.split("\n")
                    if line.strip()
                )

    return all_lines

def main():

    embed_watermark(
        input_pdf_path="test_pages/sample.pdf",
        batch_id=47,
        output_pdf_path="output/embed_demo.pdf"
    )

if __name__ == "__main__":
    main()
