from django.urls import path
from . import views

app_name = 'ei'

urlpatterns = [
    path('<int:question_pk>/answer/<int:answer_pk>/', views.answer_delete, name='answer_delete'),
    path('<int:question_pk>/answer/', views.answer_create, name='answer_create'),
    path('<int:question_pk>/detail/', views.detail, name='detail'),
    path('', views.index, name='index'),
    ]
    