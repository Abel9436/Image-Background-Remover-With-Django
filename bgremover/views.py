from django.shortcuts import render
from . import forms
from rembg import remove
from PIL import Image
import os

# Create your views here
def index(request):
    if request.method == 'POST':
        form = forms.Upload(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            form.save()
            
            # Get the path of the uploaded image
            input_path = os.path.join('media', uploaded_image.name)
            RmoveBg(input_path)
            mybool = True
            output_path = 'media/outputs/removed.png'
            return render(request, 'bgremover/index.html', {'mybool': mybool, 'output': output_path})
    else:
        form = forms.Upload()
    return render(request, 'bgremover/index.html', {'form': form})

def RmoveBg(input_path):
    input_path = os.path.join('media', input_path)
    output_path = 'media/outputs/removed.png'
    
    input_image = Image.open(input_path)
    output = remove(input_image)
    
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    
    output.save(output_path)