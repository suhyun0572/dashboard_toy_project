from django.shortcuts import render, redirect
from .forms import TrailerForm

# Create your views here.


def test(request):
    return render(request,'chart.html',{'test':123})

def trailerAdd(request):
    print("------------------------")
    print("test")
    print(request)
    if request.method == 'POST':
        form = TrailerForm(request.POST)
        if form.is_valid():
            print("this is form :" )
            print(form.cleaned_data)
            # form.save()
            return redirect('test')
        else:
            print('not valid')
            return redirect('test')
    else:
        form = TrailerForm()
        return render(request, 'trailer_add.html', {'form':form})