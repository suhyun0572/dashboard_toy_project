from django.shortcuts import render, redirect, get_object_or_404
from .forms import TrailerForm
from .models import trailers
# Create your views here.


def home(request):
    datas = trailers.objects.first()
    return render(request,'chart/index.html',{'test':datas})

def trailerAdd(request):
    print("------------------------")
    print("test")
    print(request)
    if request.method == 'POST':
        form = TrailerForm(request.POST)
        if form.is_valid():
            print("this is form :" )
            print(form.cleaned_data)
            form.save()
            print("------------------------------------------------------" )
            # return render(request,'chart:trailerAdd')
            return redirect('chart:trailerAdd')
        else:
            print('not valid')
            return redirect('chart:trailerAdd')
    else:
        form = TrailerForm()
        datas = trailers.objects.all()
        return render(request, 'chart/trailer_add.html', {'form':form, 'items':datas})

def trailerDelete(request,plate):
    delete_obj = trailers.objects.get(plate=plate)
    delete_obj.delete()
    return redirect('chart:trailerAdd')

def trailerEdit(request,plate):
    change = get_object_or_404(trailers,plate=plate)
    if request.method == 'POST':
        print('post arrived')
        form = TrailerForm(request.POST, instance=change)
        
        if form.is_valid():
            print('isvaild!')
            print(form.cleaned_data)
            form.save()
            return redirect('chart:trailerAdd')
        else:
            print(form.cleaned_data)
            print('not vaild!')
            return render(request,'chart/trailerEdit.html',{'items' : trailers.objects.get(plate=plate)})
    else:
        item = trailers.objects.get(plate=plate)
        return render(request,'chart/trailerEdit.html',{'items' : item})
    