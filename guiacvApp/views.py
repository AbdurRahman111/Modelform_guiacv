from django.shortcuts import render, redirect
from .forms import submit_form_register
from django.contrib import messages
from .models import form_register
# Create your views here.

def index(request):
    return render(request, 'index.html')

def submit_form(request):
    if request.method == 'POST':
        form = submit_form_register(request.POST, request.FILES)
        print(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added !!')
            return redirect('submit_form')
        else:
            messages.success(request, 'Fail to Add !!')
            return redirect('submit_form')
    else:
        form = submit_form_register()
        context={
            'form':form
        }
        return render(request, 'submit_form.html', context)

def see_all(request):
    all_person = form_register.objects.all()

    context2 = {
        'all_person':all_person
    }
    return render(request, 'see_all.html', context2)


def details_person(request, pk):
    get_person = form_register.objects.get(id=pk)
    context3 = {
        'get_person':get_person
    }
    return render(request, 'details_person.html', context3)

def edit_person(request, pk):
    get_person = form_register.objects.get(id=pk)

    form1 = submit_form_register(instance=get_person)

    if request.method == 'POST':
        form = submit_form_register(request.POST, request.FILES, instance=get_person)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated !!')
            return redirect('see_all')

    context4 = {
        'form1':form1
    }
    return render(request, 'edit_person.html', context4)

def delete_person(request, pk):
    get_person = form_register.objects.get(id=pk)
    if request.method=="POST":
        get_person.delete()
        messages.success(request, 'You Have Successfully Deleted !!!')
        return redirect('see_all')
    context4 = {
        'get_person': get_person
    }
    return render(request, 'delete_person.html', context4)