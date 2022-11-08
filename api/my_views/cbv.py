from msilib.schema import ServiceInstall
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import Http404
from rest_framework.permissions import IsAuthenticated
from ..models import Interview, Subject, Temp_subj, Template
from ..serializers import InterviewSerializer, SubjectMerializer, SubjectSerializer, Temp_SubjMerializer, TemplateSerializer

class InterviewListAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        interviews = Interview.objects.all()
        serilizer = InterviewSerializer(interviews,many=True)
        #companies_json = [company.to_json() for company in companies]
        return Response(serilizer.data)
    def post(self,request):
        serilizer = InterviewSerializer(data=request.data)
       
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)

class TemplateListAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        templates = Template.objects.all()
        serilizer = TemplateSerializer(templates,many=True)
        #companies_json = [company.to_json() for company in companies]
        return Response(serilizer.data)
    def post(self,request):
        serilizer = TemplateSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)

class SubjectListAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        subjects = Subject.objects.all()
        serilizer = SubjectMerializer(subjects,many=True)
        #companies_json = [company.to_json() for company in companies]
        return Response(serilizer.data)
    def post(self,request):
        serilizer = SubjectMerializer(data=request.data)
       
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)

class Temp_SubjListAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        temp_subjs = Temp_subj.objects.all()
        serilizer = Temp_SubjMerializer(temp_subjs,many=True)
        #companies_json = [company.to_json() for company in companies]
        return Response(serilizer.data)
    def post(self,request):
        serilizer = Temp_SubjMerializer(data=request.data)
       
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)



class InterviewDetailAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self,pk):
        try:
           return Interview.objects.get(id=pk)
        except Interview.DoesNotExist as e:
           raise Http404
    
    def get(self,request,pk=None):
        interview = self.get_object(pk)
        serilizer = InterviewSerializer(interview)
        return Response(serilizer.data)
    
    def put(self,request,pk=None):
        interview = self.get_object(pk)
        serilizer = InterviewSerializer(instance=interview, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)
    
    def delete(self,request,pk=None):
        interview = self.get_object(pk)
        interview.delete()
        return Response({'message': 'this interview is deleted'}, status=204)

class TemplateDetailAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self,pk):
        try:
            return Template.objects.get(id=pk)
        except Template.DoesNotExist as e:
            raise Http404

    def get(self,request,pk=None):
        vacancy = self.get_object(pk)
        serializer = TemplateSerializer(vacancy)
        return Response(serializer.data) 
    
    def put(self,request,pk=None):
        template = self.get_object(pk)
        serializer = TemplateSerializer(instance=template,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk=None):
        template = self.get_object(pk)
        template.delete()
        return Response({'message': 'this template is deleted'}, status=204)