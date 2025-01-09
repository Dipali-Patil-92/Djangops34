from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from msgapp.models import Message

# Create your views here.
def about(request):
    return HttpResponse("This is from About Page")

def delete(request,eid):
    m=Message.objects.filter(id=eid)
    #print(m)
    m.delete()
    #return HttpResponse("Employee id is: "+eid)
    return redirect('/dashboard')

class ContactForm(View):
    def get(self,request,eid):
        #return HttpResponse("This is from Class Base view")
        return HttpResponse("Employee id is: "+eid)

def hello(request):
    #x='Itvedant'
    d={}
    d['x']='Itvedant'
    d['y']=[10,20,30]
    d['a']=10
    d['b']=20
    #d={'x':'itvedant'}
    #return render(request,'hello.html',{'x':'itvedant'})

    lst=[{'id':1,'name':'hardik','city':'pune'},{'id':2,'name':'Divya','city':'Jalgaon'},{'id':3,'name':'Medhansh','city':'pune'}]
    d['data']=lst
    return render(request,'hello.html',d)

def main(request):
    return render(request,'main.html')

def product(request):
    return render(request,'product.html')

def cart(request):
    return render(request,'cart.html')

def message(request):
    #print(request.method)
    if request.method=='GET':
        return render(request,'message.html')
    else:
        n=request.POST['uname']
        e=request.POST['uemail']
        mob=request.POST['mob']
        msg=request.POST['msg']
        '''print(n)
        print(e)
        print(m)
        print(msg)'''

        m=Message.objects.create(uname=n,email=e,mob=mob,msg=msg)
        m.save()
        return HttpResponse("Data Fetched..!!")

def dashboard(request):
    m=Message.objects.all()
    #print(m)
    context={}
    context['data']=m
    #return HttpResponse("Data Fetched from database..!!")
    return render(request,'dashboard.html',context)

def edit(request,eid):
    if request.method == 'GET':
        m=Message.objects.filter(id=eid)
        #print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)

    else:
        n=request.POST['uname']
        e=request.POST['uemail']
        mob=request.POST['mob']
        msg=request.POST['msg']
        '''print(n)
        print(e)
        print(mob)
        print(msg)'''
        m=Message.objects.filter(id=eid)
        m.update(uname=n,email=e,mob=mob,msg=msg)
        return redirect('/dashboard')