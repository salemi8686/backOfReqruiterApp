from dataclasses import field
from http.client import NOT_MODIFIED
from re import template
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Temp_subj, Template,Interview,Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id','name','grade','description','feedback')
        read_only_fields = ('id',)
        
class Temp_SubjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp_subj
        fields = ('name','subject')

class TemplateSerializer(serializers.ModelSerializer):
    subjects = Temp_SubjSerializer(many=True,read_only=True)
    class Meta:
        model = Template
        fields = ('id','title','subjects')
        read_only_fields = ('id',)

class InterviewSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True,read_only=True)

    class Meta:
        model = Interview
        fields = ('id','candidate_name','level','sub_size','subjects')
        read_only_fields = ('id',)

class SubjectMerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    grade = serializers.CharField()
    description = serializers.CharField()
    feedback = serializers.CharField()
    interview = serializers.IntegerField(source = 'interview.id')

    def create(self, validated_data):
        n_interview = validated_data.get('interview')
        n_id = n_interview.get('id')
        minterview = Interview.objects.get(id=n_id)
        subject = Subject.objects.create(name = validated_data.get('name'),grade=validated_data.get('grade'),description = validated_data.get('description'),feedback = validated_data.get('feedback'),interview=(minterview))
        return subject
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.grade = validated_data.get('grade')
        instance.description = validated_data.get('description')
        instance.salary = validated_data.get('feedback')
        n_interview = validated_data.get('interview')
        n_id = n_interview.get('id')
        minterview = Interview.objects.get(id=n_id)
        instance.interview = minterview
        instance.save()
        return instance

class Temp_SubjMerializer(serializers.Serializer):
    name = serializers.CharField()
    subject = serializers.CharField()
    template = serializers.IntegerField(source = 'template.id')

    def create(self, validated_data):
        n_template = validated_data.get('template')
        n_id = n_template.get('id')
        mtemplate = Template.objects.get(id=n_id)
        temp_subj = Temp_subj.objects.create(name = validated_data.get('name'),subject=validated_data.get('subject'),template=(mtemplate))
        return temp_subj
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.subject = validated_data.get('subject')
        n_template = validated_data.get('template')
        n_id = n_template.get('id')
        mtemplate = Template.objects.get(id=n_id)
        instance.template = mtemplate
        instance.save()
        return instance
