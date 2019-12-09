from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pymongo
from grade.amount_stat import amount_pathfinding



def hello_world(request):
    if request.GET:
        Amount = int(request.GET.get('Amount', ''))
        A = request.GET.get('A', '')
        B = request.GET.get('B', '')
        C = request.GET.get('C', '')
        D = request.GET.get('D', '')
        skip_dict = {"A":int(A), "B":int(B), "C":int(C), "D":int(D)}  #check

        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client['test']
        grade = db['grade_stat']
        results = grade.find().sort('category', pymongo.ASCENDING)
        tem_amount_list = []
        grade_rst = {}
        todo_category = 'A'

        for r in results:
            if not r['category'] == todo_category:
                tem_rst = amount_pathfinding(tem_amount_list , Amount,skip_dict[todo_category])
                grade_rst[todo_category] = tem_rst
                tem_amount_list = []
                todo_category = r['category']

            tem_amount_list.append(r['amount'])


        return JsonResponse(grade_rst)
    else:
        return render(request, 'hello_world.html')


# Create your views here.
