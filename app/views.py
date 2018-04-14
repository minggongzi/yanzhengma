#coding=utf-8

from django.shortcuts import render,redirect,HttpResponse
from io import BytesIO
from utils import  check_code
from utils.check_code import create_validate_code



def index(request):
    return render(request,'index.html')
def haha(request):
    f =BytesIO()
    img,code =create_validate_code()
    img.save(f,'PNG')
    return HttpResponse(f.getvalue())