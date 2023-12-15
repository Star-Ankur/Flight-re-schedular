from django.shortcuts import render,redirect
from django.http import JsonResponse
from flight_reschedular.forms import StudentForm 
from django.http import FileResponse, HttpResponse
from .models import *
from .mycode import show
import pandas as pd
# from django.views.csrf import cs

# Create your views here.
def home(request):
    student = StudentForm()
    return render(request, 'generate.html', {'form':student})

def request_page(request):
    if (request.method == 'POST'):
        file  = request.FILES.get('input1')
        print(request.POST)
        # print(str(file.read()))
        df = pd.read_csv(file)
        df = df.head()

        # print(request.FILES.get('input1'))
        # with open(file) as f:
        #     print(f.read())
        #     f.close()
#   if(request.GET.get('mybtn')):
#     output = show( int(request.GET.get('option')) )
#     file = request.GET.get('input1')
#     print(file)
#     print(type(request.body))
# #     print(output)
#     response = FileResponse(df.to_csv('output.csv', index=False), content_type='application/octet-stream')

#     # Set the file name for download
#     response['Content-Disposition'] = 'attachment; filename="generated_file.csv"'

        csv_string = df.to_csv(index=False)

        # Create a Django HttpResponse object with CSV content as a file attachment
        response = HttpResponse(csv_string, content_type='text/csv')

    return response
    # return render(request,'check.html', {'value': '3'})


def generate(request):
    if request.method=='POST' :
        file1  = request.FILES.get('input1')
        file2 = request.FILES.get('input2')
        file3  = request.FILES.get('input3')

        rule1 = request.POST.get('check1')
        rule2 = request.POST.get('check2')
        rule3 = request.POST.get('check3')
        rule4 = request.POST.get('check4')
        rule5 = request.POST.get('check5')
        rule6 = request.POST.get('check6')

        algo1 = request.POST.get('option1')
        algo2 = request.POST.get('option2')




