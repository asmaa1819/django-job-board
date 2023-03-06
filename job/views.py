from django.shortcuts import render
from .models import job

# Create your views here.
def job_list (request):
    job_list=job.objects.all()
    context={'jobs':job_list}
    return render(request,'job/job_list.html',context)

def job_detal (request,id):
    job_detal=job.objects.get(id=id)
    context={'job':job_detal}
    return render(request,'job/job_detal.html',context)
