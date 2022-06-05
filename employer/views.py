from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView,FormView
from employer.forms import Jobform,Loginform
from django.urls import reverse_lazy
from employer.models import Jobs
from django.contrib.auth.models import User
from employer.forms import Signupform
from django.contrib.auth import authenticate,login,logout


# Create your views here.
class Employer_Home_View(TemplateView):
    def get(self,request):
        return render(request,'emp-home.html')

class Addjobview(CreateView):
    model = Jobs
    form_class = Jobform
    template_name = "emp-addjob.html"
    success_url = reverse_lazy("emp-listjob")

    # def get(self,request):
    #     form=Jobform
    #     context={'form':form}
    #     return render(request,'emp-addjob.html',context)
    # def post(self,request):
    #     form=Jobform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,'emp-home.html')
    #     else:
    #         return render(request,'emp-addjob',{'form':form})

class ListJobview(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-listjob.html"

    # def get(self,request):
    #     qs=Jobs.objects.all()
    #     return render(request,"emp-listjob.html",{"jobs":qs})

class Jobdetailview(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "emp-jobdetail.html"
    pk_url_kwarg = "id"

    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,'emp-jobdetail.html',{'job':qs})

class Jobeditview(UpdateView):
    model = Jobs
    template_name = "emp-editjob.html"
    form_class = Jobform
    success_url = reverse_lazy("emp-listjob")
    pk_url_kwarg = "id"

    # def get(self,request,id):
    #     qs = Jobs.objects.get(id=id)
    #     form=Jobform(instance=qs)
    #     return render(request,"emp-editjob.html",{'form':form})
    # def post(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=Jobform(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("emp-listjob")
    #     else:
    #         return render(request,'emp-editjob.html',{'form':form})
class Jobdeleteview(DeleteView):
    model = Jobs
    template_name = "emp-deletejobs.html"
    success_url = reverse_lazy("emp-listjob")
    pk_url_kwarg = "id"

    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     qs.delete()
    #     return redirect("emp-listjob")

class Signupview(CreateView):
    model = User
    form_class = Signupform
    template_name = "user-signup.html"
    success_url = reverse_lazy("emp-home")

class Loginview(FormView):
    form_class = Loginform
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect('emp-home')
            else:
                return render(request,'login.html',{'form':form})

# to create superuser like admin - python manage.py createsuperuser
def logout_view(request,*args,**kwargs):
    logout(request)
    return redirect('user-login')

class Passwordreset(TemplateView):
    template_name = 'pwdreset.html'
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get('pwd1')
        pwd2=request.POST.get('pwd2')
        msg="password miss match"
        if pwd1!=pwd2:
            return render(request,'pwdreset.html',{'msg':msg})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd2)
            u.save()
            return redirect('user-login')

class Changepwd_view(TemplateView):
    template_name = 'changepwd.html'
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect('pwdreset')
        else:
            return render(request,self.template_name)



