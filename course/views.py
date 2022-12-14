from django.shortcuts import render,redirect
from .models import Course,Students,Instractor
from .forms import CourseForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.


def Indeview(request):
    courses=Course.objects.all()
    context={
        'courses':courses
    }
    return render(request,'index.html',context)
#crud
#CreateView

def CreateCourse(request):
    form=CourseForm()
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course:index')
    context={
        'form':form
    }
    return render(request,'create.html',context)
#UpdateView

def UpdateView(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        # Update the object with the new data from the form
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course:index')
    else:
        # Show the form for editing the object
        form = CourseForm(instance=course)
        context={
            'form': form
        }

    return render(request, 'update.html',context)


#DELETEView


def DeleteView(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        course.delete()
        return redirect('course:index')
    context={
    'course':course
    }

    return render(request, 'delete.html',context)

def StudentView(request):
    students=Students.objects.all()
    context={
        'students':students
    }
    return render(request,'student.html',context)

def InstratorView(request):
    instractors=Instractor.objects.all()
    context={
        'instractors':instractors
    }
    return render(request,'instractor.html',context)



