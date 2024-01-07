from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import Profile
from .forms import ProjectForm, ReviewForm
from .models import Project
from .utils import searchProjects, paginateProjects


# Create your views here.
def home(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'projects/index.html', context)


def project_list(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 3)
    context = {'projects': projects, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/project-list.html', context)


@login_required(login_url='login')
def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()
        project.getVoteCount
        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project-detail', pk=project.id)

    context = {'project': project, 'form': form}
    return render(request, 'projects/project-detail.html', context)


@login_required(login_url='login')
def project_create(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect('project-list')

    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url='login')
def project_update(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-list')

    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url='login')
def project_delete(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('project-list')

    context = {'project': project}
    return render(request, 'projects/project-confirm-delete.html', context)