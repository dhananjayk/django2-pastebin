from django.shortcuts import render, redirect
from .models import PasteObject
from django.views.decorators.cache import never_cache

# Create your views here.
from .forms import PasteForm

@never_cache
def index(request, *args, **kwargs):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PasteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            paste_data = form.cleaned_data.get('text')
            owner = request.user if request.user.is_authenticated else None
            new_paste = PasteObject.objects.create(text=paste_data, owner=owner)
            return redirect(new_paste)


        # if a GET (or any other method) we'll create a blank form
    else:
        url_key = kwargs.get('url_key', None)
        if url_key:
            query = PasteObject.objects.filter(url_key=url_key) 
            if query.exists():
                text = query.values('text').get()
            else:
                return redirect('index')
        else:
            text = ''
        
        form = PasteForm(initial=text)
    return render(request, 'djpaste/index.html', {'form': form},)

@never_cache
def authorize(request):
    return redirect('index')