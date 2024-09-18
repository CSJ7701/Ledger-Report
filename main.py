from transaction import Transaction
from pdf import pdf_title
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime

date=datetime.today().strftime("%d%b%Y")
ledger_file="/home/csj7701/Personal/Ledger/Main.ledger"
ledger_command=f"ledger -f {ledger_file} csv"
output_file=f"/home/csj7701/Personal/Ledger/Reports/CJohnson-Report-{date}"

canvas=canvas.Canvas(output_file, pagesize=letter)

pdf_title(canvas)
