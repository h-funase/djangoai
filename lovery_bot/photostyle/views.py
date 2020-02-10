from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader



def select(request):
    template = loader.get_template('photostyle/select.html')
    context = {}
    return HttpResponse(template.render(context, request))

def generate(request):
    if not request.method == 'POST':
        return
        redirect('photostyle:select')

    form = PhotoForm(request.POST, request.FILES)
    if not form.is_valid():
        raise ValueError('Formが不正です')

    photo = Photo(image=form.cleaned_data['image'])

    template = loader.get_template('photostyle/result.html')

    context = {
        'photo_name': photo.image.name,
        'photo_data': photo.image_src(),
      
    }

    return HttpResponse(template.render(context, request))

