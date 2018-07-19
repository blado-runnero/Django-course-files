from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App!!</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'apptwo/help.html',context=helpdict)

def user_records_print(request):
        userss_list = Users.objects.order_by('f_name')
        user_dict = {'users_data': userss_list}
        return render(request,'apptwo/users.html', context=user_dict)
