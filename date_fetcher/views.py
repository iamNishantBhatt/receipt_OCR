from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from . import image_process


# Create your views here.


def image_result(request):
    url = request.session.get('imgURL')
    content = image_process.img_preprocessing(url)

    return render(request, 'image_result.html', {'content': [content]})


def image_view(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        request.session['imgURL'] = url
        return redirect('image_result')

    return render(request, 'image_form.html')
