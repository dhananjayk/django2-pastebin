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
            paste_name = form.cleaned_data.get('paste_name')
            paste_expiration = form.cleaned_data.get('paste_expiration')
            private_paste = form.cleaned_data.get('private_paste')
            syntax_highlighting = form.cleaned_data.get('syntax_highlighting')
            owner = request.user if request.user.is_authenticated else None
            new_paste = PasteObject.objects.create(text=paste_data, owner=owner)
            new_paste = PasteObject.objects.create(text=paste_data, owner=owner, paste_name=paste_name,
                                                   expiration_date=paste_expiration,
                                                   syntax_highlighting=syntax_highlighting, private=private_paste)
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