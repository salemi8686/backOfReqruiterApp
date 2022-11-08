import imp
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.http.request import HttpRequest
from django.http.response import HttpResponse,JsonResponse

from ..serializers import InterviewSerializer, TemplateSerializer

from ..models import Interview, Template

@api_view(['GET','POST'])
def interview_list(request):
    if request.method == 'GET':
        interviews = Interview.objects.all()
        serilizer = InterviewSerializer(interviews,many=True)
        return Response(serilizer.data,safe=False)
    elif request.method == 'POST':
        serilizer = InterviewSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse(serilizer.data)
        return Response(serilizer.errors)

@api_view(['GET','PUT',"DELETE"])
def interview_detail(request,company_id):
    try:
        interview = Interview.objects.get(id=company_id)
    except Interview.DoesNotExist as e:
        return Response({'message' : str(e)},status=400)
    
    if request.method == 'GET':
        serilizer = InterviewSerializer(interview)
        return Response(serilizer.data)
    elif request.method == 'PUT':
        serilizer = InterviewSerializer(instance=interview, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)
    elif request.method == 'DELETE':
        interview.delete()
        return Response({'message': 'this product is deleted'}, status=204)

@api_view(['GET','POST'])
def template_list(request):
    if request.method == 'GET':
        template = Template.objects.all()
        serializer = TemplateSerializer(template,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def vacancy_detail(request,vacancy_id):
    try:
        template = Template.objects.get(id=vacancy_id)
    except Template.DoesNotExist as e:
        return JsonResponse({'message' : str(e)},status=400)
    if request.method == 'GET':
        serializer = TemplateSerializer(template)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TemplateSerializer(instance=template,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        template.delete()
        return Response({'message': 'this vacancy is deleted'}, status=204)