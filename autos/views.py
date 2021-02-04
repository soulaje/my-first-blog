from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

from autos.models import Auto,Make
from autos.forms import MakeForm

class MainView(View):
    def get(self, request):
       mc= Make.objects.all().count()
       al=Auto.objects.all()

       ctx={'make_count': mc, 'auto_list':al}
       return render(request,'autos/auto_list.html',ctx)
# Create your views here.

class MakeView(View):
    def get(self,request):
        ml=Make.objects.all()
        ctx={'make_list':ml}
        return render(request,'autos/make_list.html',ctx)

class MakeCreate(View):
    template='autos/make_form.html'
    success_url=reverse_lazy('autos:all')

    def get(self,request):
        form=MakeForm()
        ctx={'form':form}
        return render(request,self.template,ctx)

    def post(self, request):
        form=MakeForm(request.POST)
        if not form.is_valid():
            ctx={'form': form}
            return (request,self.template,ctx)
        make=form.save()
        return redirect(self.success_url)

class AutoCreate(CreateView):
    model=Auto
    fields='__all__'
    success_url=reverse_lazy('autos:all')

class MakeUpdate(View):
    model=Make
    success_url=reverse_lazy('autos:all')
    template='autos/make_form.html'

    def get(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        form=MakeForm(instance=make)
        ctx={'form':form}
        return render(request,self.template,ctx)

    def post(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        form=MakeForm(request.POST,instance=make)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,self.template,ctx)
        form.save()
        return redirect(self.success_url)

class AutoUpdate(UpdateView):
    model=Auto
    fields='__all__'
    success_url=reverse_lazy('autos:all')


class MakeDelete(View):
    model=Make
    success_url=reverse_lazy('autos:all')
    template='autos/make_confirm_delete.html'


    def get(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        form=MakeForm(instance=make)
        ctx={'make':make}
        return render(request,self.template,ctx)

    def post(self,request,pk):
        make=get_object_or_404(self.model,pk=pk)
        make.delete()
        return redirect(self.success_url)
class AutoDelete(DeleteView):
    model=Auto
    fields='__all__'
    success_url=reverse_lazy('autos:all')


