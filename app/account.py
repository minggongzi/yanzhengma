

from django.shortcuts import render,redirect,HttpResponse
from io import BytesIO
from utils import  check_code
from utils.check_code import create_validate_code

def check_code111(request):
    img, code = check_code.create_validate_code()  #执行check_code文件内的create_validate_code()方法
    stream = BytesIO() #建立一个内存区域
    img.save(stream, 'PNG')  #以PNG格式存入内存
    request.session['Check_code'] = code  #验证码存入session
    return HttpResponse(stream.getvalue())  #把生成的图片返回给img

