from django.shortcuts import render

from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse , JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def student_details_view(request,pk):
    student = Student.objects.get(id=pk)
    serializeStu = StudentSerializer(student)
    return JsonResponse(serializeStu.data)

def all_students_view(request):
    student = Student.objects.all()
    serializeList = StudentSerializer(student, many = True)
    return JsonResponse(serializeList.data,safe=False)

@csrf_exempt
def student_create(request):
    if(request.method == 'POST'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serialize = StudentSerializer(data = pythonData)
        if(serialize.is_valid()):
            msg = {'msg':'added successfully'}
            serialize.save()
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serialize.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if(request.method =='PUT'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_Data = JSONParser().parse(stream)
        id =python_Data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=python_Data,partial = True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'updated successfully'}
            json_response  = JSONRenderer().render(msg)
            return HttpResponse(json_response,content_type ='application/json')
        json_response = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_response,content_type='application/json')
    
    if request.method == 'DELETE':
       json_data = request.body
       stream = io.BytesIO(json_data)
       python_data = JSONParser().parse(stream)
       id = python_data.get('id')
       stu = Student.objects.get(id=id)
       stu.delete()
       msg={'msg':'deleted successfully'}
       json_response = JSONRenderer().render(msg)
       return HttpResponse(json_response,content_type='application/info')    
    


