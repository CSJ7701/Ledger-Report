from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def pdf_title(c):
    width, height = letter
    date=datetime.today()

    # Add title page
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 100, "Monthly Expense Report")
    c.setFont("Helvetica", 18)
    c.drawString(100, height - 150, "Prepared by: Your Name")
    c.drawString(100, height - 200, "Date: " + str(date))

    c.showPage()

    c.save()

