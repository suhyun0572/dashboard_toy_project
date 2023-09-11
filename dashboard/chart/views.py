from django.shortcuts import render, redirect
from .forms import TrailerForm

# Create your views here.


def test(request):
    return render(request,'chart.html',{'test':123})

def trailerAdd(request):
    print("test")
    print(request)
    if request.method == 'POST':
        form = TrailerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test')
        else:
            return redirect('test')
    else:
        form = TrailerForm()
        return render(request, 'trailerAdd', {'form':form})