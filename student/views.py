from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Student
import requests
import json
from .serializers import AddStudentSerializer
from rest_framework import status
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | line_no=%(lineno)d | %(message)s',
                    filename='C:/Users/miracle/Desktop/mongo_django/mongo_project/myapp.log',
                    filemode='a')


def getAllStudents(request):
    # print ("URL Params :",request.META['QUERY_STRING'])
    age = request.GET.get('age')
    name = request.GET.get('name')
    if age:
        student_data = Student.objects.all().filter(Age=age)
    elif name:
        student_data = Student.objects.all().filter(Name=name)
    elif age and name:
        student_data = Student.objects.all().filter(Age=age).filter(Name=name)
    else:
        student_data = Student.objects.all()
    # for field in student_data:
    student_list = list(student_data)
    # return HttpResponse(student_list)
    data = serializers.serialize('json', student_list)
    # return JsonResponse(student_list, safe=False)
    return HttpResponse(data, content_type='application/json')


def addStudent(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        req = json.loads(data)
        serializer = AddStudentSerializer(data={'Name': req['Name'],'Age':req['Age'],'RollNumber':req['RollNumber']})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Info":"Data Inserted Successfully"}, status=status.HTTP_200_OK)
        return JsonResponse({"Info":"Data Invalid"+str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Check HTTP method")


def updateStudent(request):
    if request.method == 'PUT':
        data = request.body.decode('utf-8')
        req = json.loads(data)
        student_data = Student.objects.all().filter(Name=req['Name']).update(Age=req['Age'])
        print(student_data)
        if student_data > 0:
            return JsonResponse({"Info":"Data Updated Successfully"}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"Info":"No Records found to Update"}, status=status.HTTP_400_BAD_REQUEST)


def deleteStudent(request):
    if request.method == 'DELETE':
        data = request.body.decode('utf-8')
        req = json.loads(data)
        student_data = Student.objects.all().filter(Name=req['Name']).delete()
        # print(student_data[0])
        if student_data[0] > 0:
            return JsonResponse({"Info":"Data Deleted Successfully"}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"Info":"Failed to delete data"}, status=status.HTTP_400_BAD_REQUEST)
        

def getCurrency(request):
    print("Converting Currency")
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=INR&apikey=XZ5MD84ANCXI9KZR"
    result = (requests.get(url))
    logging.info('Got Response from ALPHAVANTAGE')
    return HttpResponse(result, content_type='application/json')
