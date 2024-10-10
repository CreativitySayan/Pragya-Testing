# certificates/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Certificate
from .forms import CertificateSearchForm
import pandas as pd
from django.core.files.storage import default_storage

def home(request):
    return render(request, 'home.html') 

def upload_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        
        # Check if the file is an Excel file
        if not excel_file.name.endswith('.xls') and not excel_file.name.endswith('.xlsx'):
            return JsonResponse({"status": "Invalid file format. Please upload an Excel file."})

        try:
            # Save the file to the uploads directory
            file_path = default_storage.save(f'uploads/{excel_file.name}', excel_file)
            
            # Load the Excel file using pandas
            excel_data = pd.read_excel(file_path)

            # Validate the required columns in the Excel file
            required_columns = ['Certificate Number', 'Participant Name', 'Category', 'Event Name', 'Date']
            if not all(column in excel_data.columns for column in required_columns):
                raise ValidationError("Excel file is missing required columns.")
            
            # Iterate through rows and save them in the database
            for _, row in excel_data.iterrows():
                Certificate.objects.create(
                    certificate_number=row['Certificate Number'],
                    participant_name=row['Participant Name'],
                    category=row['Category'],
                    event_name=row['Event Name'],
                    date=row['Date']
                )
            return JsonResponse({"status": "Excel file uploaded and data saved successfully."})
        
        except Exception as e:
            return JsonResponse({"status": f"Error processing file: {e}"})
    
    return render(request, 'upload_excel.html')
def check_certificate(request):
    if request.method == 'POST':
        form = CertificateSearchForm(request.POST)
        if form.is_valid():
            certificate_number = form.cleaned_data['certificate_number']
            certificate = Certificate.objects.filter(certificate_number=certificate_number).first()
            if certificate:
                return render(request, 'check_certificate.html', {'certificate': certificate, 'valid': True})
            else:
                return render(request, 'check_certificate.html', {'valid': False})
    else:
        form = CertificateSearchForm()
    return render(request, 'check_certificate.html', {'form': form})
