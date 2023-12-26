from django.shortcuts import render
from .models import Project


# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project-list.html', context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'projects/project-detail.html', context)