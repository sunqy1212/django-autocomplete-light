# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,request,HttpRequest
from bdgqpt.models import *
from django.views.generic.edit import CreateView,UpdateView
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib import messages
from bdgqpt.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.views.decorators.csrf import csrf_exempt
from dal import autocomplete
import datetime
from django_ajax.decorators import ajax




 # Create your views here.
#主页
def index(request):
    return render(request, 'bdgqpt/caozuopiao/caozuopiao_index.html')

#操作票主页
def caozuopiao_list(request):
    queryset_list = CaoZuoPiao.objects.all()
    paginator = Paginator(queryset_list, 10)   # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
    'caozuopiao_list': queryset,
    'page_request_var': page_request_var
    }
    return render(request,'bdgqpt/caozuopiao/caozuopiao_index.html', context, context_instance = RequestContext(request))


def caozuopiao_create(request,p):
    if not request.user.is_authenticated():
        return render(request, 'bdgqpt/login.html')
    else:
        if p=='yuling':
            form=CaoZuoPiaoForm_yuling(request.POST or None)
        elif p=='zhengling':
            form=CaoZuoPiaoForm_zhengling(request.POST or None)
        title="登记操作票"
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            messages.success(request,"操作票登记成功")
            return redirect('bdgqpt:caozuopiaohomepage')                 
        context = {
        "form": form,
        "title":title, 
        }
        return render(request, 'bdgqpt/caozuopiao/caozuopiao_create_form.html', context, context_instance=RequestContext(request))

class NameAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # if not self.request.user.is_authenticated():
        #     return UserProfile.objects.none()
        qs = UserProfile.objects.all()
        if self.q:
            qs = qs.filter(full_name__icontains=self.q)
        return qs
   

def caozuopiao_detail(request,id=None):
    instance=get_object_or_404(POST,id=id)
    context={
    "instance":instance
    }
    return redner(request,"bdgqpt/caozuopiao_detail.html",context)


def caozuopiao_update(request, id=None):
    if not request.user.is_authenticated():
        return render(request, 'bdgqpt/login.html')
    else:       
        instance = get_object_or_404(CaoZuoPiao, id=id)
        form = CaoZuoPiaoForm_update(request.POST or None,instance=instance)
        
        title="修改操作票"
        if form.is_valid():
            instance.save()
            messages.success(request,"修改成功")
            return redirect('bdgqpt:caozuopiaohomepage')
        context = {
            "form": form,
            "title":title,
        }
        return render(request, 'bdgqpt/caozuopiao/caozuopiao_update_form.html', context)


def caozuopiao_delete(request,id=None):
    instance=get_object_or_404(CaoZuoPiao,id=id)
    instance.delete()
    messages.success(request,"删除成功")
    return redirect('bdgqpt:caozuopiaohomepage')

from django_modalview.generic.edit import ModalCreateView
from django_modalview.generic.component import ModalResponse
class caozuopiaoCreateModalView(ModalCreateView):
    def __init__(self,*args,**kwargs):
        super(caozuopiaoCreateModalView,self).__init__(*args,**kwargs)
        self.title='操作票登记'
        self.form_class=CaoZuoPiaoForm_yuling
        self.content_template_name='bdgqpt/caozuopiao/caozuopiao_create_form_modal.html'
        #self.redirect_to = '/caozuopiaohomepage/'
    def form_valid(self, form, **kwargs):
        self.response = ModalResponse("Good game", "success")
        return super(caozuopiaoCreateModalView, self).form_valid(form, **kwargs)



class caozuopiaoUpdate(UpdateView):
    model = CaoZuoPiao
    fields = '__all__'

class Addcaozuopiao2(CreateView):
    model = CaoZuoPiao
    fields = '__all__'
    
