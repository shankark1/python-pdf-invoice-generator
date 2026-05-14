from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

print("PDF Invoice Generator")

customer = input("Enter customer name: ")

item = input("Enter item name: ")

price = float(input("Enter item price: "))

quantity = int(input("Enter quantity: "))

total = price * quantity

file_name = "invoice.pdf"

pdf = canvas.Canvas(file_name, pagesize=letter)

pdf.setFont("Helvetica", 16)
pdf.drawString(200, 750, "INVOICE")

pdf.setFont("Helvetica", 12)

pdf.drawString(50, 700, "Customer Name: " + customer)

pdf.drawString(50, 650, "Item: " + item)

pdf.drawString(50, 620, "Price: $" + str(price))

pdf.drawString(50, 590, "Quantity: " + str(quantity))

pdf.drawString(50, 560, "Total: $" + str(total))

pdf.save()

print("Invoice PDF created successfully.")