from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token  
from .my_views.cbv import InterviewDetailAPIView, InterviewListAPIView, SubjectListAPIView, Temp_SubjListAPIView, TemplateDetailAPIView, TemplateListAPIView




urlpatterns = [
    path('login/',obtain_jwt_token),
    path('interviews/',InterviewListAPIView.as_view()),
    path('interviews/<int:pk>/',InterviewDetailAPIView.as_view()),
    path('subjects/',SubjectListAPIView.as_view()),
    path('temp_subjects/',Temp_SubjListAPIView.as_view()),
    path('templates/',TemplateListAPIView.as_view()),
    path('templates/<int:pk>/',TemplateDetailAPIView.as_view()),
    
]









