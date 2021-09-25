from django.urls import path, include
from quiz_app import views

#from django.views.generic import TemplateView

urlpatterns = [
    path('choosequiztype/',views.choose_quiz_type),
    path('chosenquiztype/<str:chosen_type>',views.chosen_quiz_type),]
    #path('',TemplateView.as_view(template_name='index.html'))
