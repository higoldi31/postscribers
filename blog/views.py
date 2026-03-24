from django.shortcuts import render
from .models import PostModel
from .forms import PostModelForm
# Create your views here.
def index(request):
    posts=PostModel.objects.all()
    form=PostModelForm()
    context={
        'posts':posts,
        'form':form,
    }

    return render(request,'blog/index.html',context)