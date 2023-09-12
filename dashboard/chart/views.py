from django.shortcuts import render, redirect
from .forms import TrailerForm
from .models import trailers
# Create your views here.


def test(request):
    datas = trailers.objects.first()
    return render(request,'chart.html',{'test':datas})

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
            return redirect('test')
        else:
            print('not valid')
            return redirect('test')
    else:
        form = TrailerForm()
        datas = trailers.objects.all()
        return render(request, 'trailer_add.html', {'form':form, 'items':datas})