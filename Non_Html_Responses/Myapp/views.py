from django.shortcuts import render
# Create your views here.
# demo/views.py
import csv
import io
import zipfile
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
from reportlab.lib import colors

def index(request):
    return render(request, 'Myapp/index.html')

def image_response(request):
    # Create a simple image using PIL
    image = Image.new('RGB', (200, 200), color='yellow')
    draw = ImageDraw.Draw(image)
    draw.text((40, 70), "FSD", fill='blue')
    draw.text((40, 80), "handled by Dr.Sm.Badhusha", fill='blue')
    response = HttpResponse(content_type='image/png')
    image.save(response, 'PNG')
    return response

def pdf_response(request):
    # Create a PDF using ReportLab
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica-Bold", 36)
    p.setFillColor(colors.magenta)
    p.drawString(100, 400, "Full Stack Development")
    p.setFont("Helvetica-Bold", 18)
    p.setFillColor(colors.blue)
    p.drawString(100, 375, "Content delivery by Dr.Sm.Badhusha")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='example.pdf')

def csv_response(request):
    # Create a CSV file
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Age', 'Country'])
    writer.writerow(['Alice', 28, 'USA'])
    writer.writerow(['Bob', 35, 'Canada'])
    writer.writerow(['Charlie', 42, 'UK'])
    return response

def zip_response(request):
    # Create a ZIP file containing multiple files
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        zip_file.writestr('file1.txt', 'This is file 1')
        zip_file.writestr('file2.txt', 'This is file 2')
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='archive.zip')

def plot_response(request):
    # Create a plot using Matplotlib
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('x')
    plt.ylabel('y')
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return FileResponse(buffer, content_type='image/png')
