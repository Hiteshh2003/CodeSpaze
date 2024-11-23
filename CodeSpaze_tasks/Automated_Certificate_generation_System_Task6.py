from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
import os
import qrcode

def generate_certificate(name, title, date, output_dir):
    """
    Generate a professional-looking certificate using ReportLab.
    """
    # Set up file name and canvas
    output_file = os.path.join(output_dir, f"{name}_certificate.pdf")
    c = canvas.Canvas(output_file, pagesize=landscape(letter))

    # Add background template
    template = "D:/Downloads/blue-gold-geometry-modern-certificate-border-frame_257504-424.jpg"  # Replace with your certificate template path
    if os.path.exists(template):
        c.drawImage(template, 0, 0, width=11 * 72, height=8.5 * 72)

    # Add the company logo
    logo_path = "codespaze_logo.png"  
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 30, 480, width=120, height=120)  

    # Add the main heading (Certificate of Completion)
    c.setFont("Times-Bold", 42)
    c.setFillColor(colors.darkblue)
    c.drawCentredString(415, 440, "Certificate of Completion")

    # Add a subheading for decoration
    c.setFont("Times-Italic", 18)
    c.setFillColor(colors.black)
    c.drawCentredString(415, 410, "This is proudly presented to")

    # Add recipient's name (larger font for emphasis)
    c.setFont("Times-Bold", 32)
    c.setFillColor(colors.black)
    c.drawCentredString(415, 370, name)

    # Add the achievement description
    c.setFont("Times-Roman", 20)
    c.drawCentredString(415, 330, f"For successfully completing the {title} course")

    # Add completion date
    c.setFont("Helvetica", 16)
    c.setFillColor(colors.black)
    c.drawCentredString(415, 290, f"Completion Date: {date}")

    # Add QR code (verification or additional information)
    qr_data = f"https://www.codespaze.com/certificate/{name}"  #we have to replace this with the actual link this is demo link 
    qr_code = qrcode.make(qr_data)
    qr_code_path = "temp_qr.png"
    qr_code.save(qr_code_path)

    # Updated QR Code Position
    c.drawImage(qr_code_path, 50, 50, width=100, height=100)  

    # Add footer (authorized signatory section)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.black)
    c.drawString(100, 100, "_____________________")
    c.drawString(150, 80, "Authorized Signature")
    c.drawCentredString(415, 80, "CodeSpaze")

    # Save PDF
    c.save()

    # Remove temporary QR code file
    if os.path.exists(qr_code_path):
        os.remove(qr_code_path)

    return output_file

def submit_details():
    """
    Handle user input and generate the certificate.
    """
    name = name_entry.get()
    title = title_entry.get()
    date = date_entry.get()

    if not name or not title or not date:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    output_dir = filedialog.askdirectory(title="Select Output Folder")
    if not output_dir:
        return
    
    try:
        file_path = generate_certificate(name, title, date, output_dir)
        messagebox.showinfo("Success", f"Certificate generated: {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate certificate: {e}")

# Set up GUI
root = Tk()
root.title("Professional Certificate Generator")

Label(root, text="Recipient's Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Certificate Title:").grid(row=1, column=0, padx=10, pady=10)
title_entry = Entry(root, width=30)
title_entry.grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Completion Date (DD/MM/YYYY):").grid(row=2, column=0, padx=10, pady=10)
date_entry = Entry(root, width=30)
date_entry.grid(row=2, column=1, padx=10, pady=10)

Button(root, text="Generate Certificate", command=submit_details).grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
