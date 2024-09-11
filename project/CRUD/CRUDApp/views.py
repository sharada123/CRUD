from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def home(request):
    s=Student.objects.all()
    context={}
    context['data']=s
    return render(request,'index.html',context)

def create(request):
    if request.method=='POST':
        sname=request.POST['sname']
        add=request.POST['add']
        mob=request.POST['mob']
        dept=request.POST['dept']
        per=request.POST['per']
        print(sname)
        s=Student.objects.create(name=sname,address=add,mobile=mob,department=dept,per=per)
        s.save()
        return redirect('/')
    else:    
     return render(request,'create.html')

def delete(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect("/")

def update(request,id):
    
    if request.method=="POST":
        sname=request.POST['sname']
        add=request.POST['add']
        mob=request.POST['mob']
        dept=request.POST['dept']
        per=request.POST['per']
        s=Student.objects.filter(id=id)
        s.update(name=sname,address=add,mobile=mob,department=dept,per=per)
        return redirect('/')
    else:
        s=Student.objects.get(id=id)
        print(s)
        context={}
        context['data']=s
        return render(request,'update.html',context)