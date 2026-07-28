from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from utils import batch_to_binary, binary_to_bits

def create_sample_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=A4)

    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(250, height - 20, "Sample Question Paper")

    # Questions
    c.setFont("Helvetica", 12)

    questions = [
        "1. What is Java?",
        "2. Explain the OSI Model.",
        "3. What is SQL?",
        "4. Define Operating System.",
        "5. Explain Binary Search."
    ]

    y = height - 70

    for question in questions:
        c.drawString(70, y, question)
        y -= 150

    c.save()

    print("PDF Generated Successfully!")

if __name__ == "__main__":
    create_sample_pdf("output/sample_question_paper.pdf")