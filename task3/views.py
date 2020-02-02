from django.shortcuts import render


def homepage(request):
    return render(request,'task3/index.html')

def res_text(request):
    return render(request,'task3/f1.html')

def res_table(request):
    return render(request,'task3/f2.html')

def res_image(request):
    return render(request,'task3/f3.html')


def res_card(request):
    return render(request,'task3/f4.html')

