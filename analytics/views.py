from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import pandas as pd
# Create your views here.

def read_csv():
    return pd.read_csv('analytics/Task_one.csv')

@api_view(['GET'])
def get_n_highest_salary (request):
   
    employees_data = read_csv()
    n  = int (request.GET.get('n'))
    n_highest_salaries = employees_data.nlargest(n, 'Salary')

    return JsonResponse(n_highest_salaries.to_dict(orient='records'), safe=False)
    

@api_view(['GET'])
def get_number_of_employees(request):
    employees_data = read_csv()
    
    try:
        department = request.GET.get('department')
    except:
        return render(request, 'analytics/error.html', {'error': 'Please provide a valid department name'})

    employees_number = employees_data[employees_data['Department'] == department].shape[0]
    return JsonResponse({'Number of Employees': employees_number})
