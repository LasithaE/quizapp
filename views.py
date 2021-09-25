from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.models import User
from quiz_app.models import *
from rest_framework import request
#from rest_framework.response import Response
from django.http import JsonResponse


@api_view(['GET'])
def choose_quiz_type(request):
    
    quiz_ids=home_quiz.objects.values_list('quiz_id')
    quiz_names=home_quiz.objects.values_list('name')
    quiz_desc=home_quiz.objects.values_list('desc')
    no_of_qs=home_quiz.objects.values_list('number_of_questions')
    
    quiz_ids=[quiz_ids[p][0] for p in range(len(quiz_ids))]
    quiz_names=[quiz_names[q][0] for q in range(len(quiz_names))]
    quiz_desc=[quiz_desc[r][0] for r in range(len(quiz_desc))]
    no_of_qs=[no_of_qs[s][0] for s in range(len(no_of_qs))]
    print(quiz_ids,quiz_names,quiz_desc,no_of_qs)
    res=[]
    for i in range(len(quiz_ids)):
        print('pppppp',{'id':quiz_ids[i],'name_of_quiz':quiz_names[i],'description':quiz_desc[i],'number_of_questions':no_of_qs[i]})
        res.append({'id':quiz_ids[i],'names_of_quiz':quiz_names[i],'description':quiz_desc[i],'number_of_questions':no_of_qs[i]})
    
    return JsonResponse(res,safe=False)



@api_view(['GET'])
def chosen_quiz_type(request,chosen_type):
    quiztype_details=home_quiz.objects.filter(quiz_id=chosen_type).values('name','number_of_questions',)
    
    quiz_details=home_question.objects.filter(quiz_type_id=chosen_type).values('question_id','question','choice_1','choice_2','choice_3','choice_4','correct_choice')
    print(quiz_details)
    #{'quiz_name':quiztype_details['name'],'questions':,'choices':{},'correct_choice':}
    return JsonResponse({})