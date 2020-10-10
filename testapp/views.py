from django.shortcuts import render,redirect
from testapp.models import employee
from testapp.forms import employeeform
# Create your views here.
def index_view(request):
    records=employee.objects.all()
    return render(request,'testapp/index.html',{'records':records})

def create_view(request):
    form=employeeform()
    if request.method=="POST":
        form=employeeform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect("/index")
    return render(request,"testapp/create.html",{'form':form})

def delete_view(request,id):
    employee1=employee.objects.get(id=id)
    employee1.delete()
    return redirect('/index')

def update_view(request,id):
    employee1=employee.objects.get(id=id)
    if request.method=='POST':
        form=employeeform(request.POST,instance=employee1)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'testapp/update.html',{'employee1':employee1})    
