from django.shortcuts import render


# Create your views here.
from .forms import PasteForm


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PasteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            pass

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PasteForm()
    return render(request, 'djpaste/index.html', {'form': form},)
