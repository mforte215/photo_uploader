import io
import qrcode
import base64
from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

def home(request):
    upload_url = request.build_absolute_uri('/upload/')
    qr = qrcode.QRCode(box_size=8, border=2)
    qr.add_data(upload_url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    qr_b64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'app/home.html', {'qr_b64': qr_b64})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = PhotoForm()
    return render(request, 'app/upload.html', {'form': form})

def view_app(request):
    photos = Photo.objects.order_by('-uploaded_at')
    return render(request, 'app/gallery.html', {'photos': photos})

def view_gallery(request):
    photos = Photo.objects.order_by('-uploaded_at')
    return render(request, 'app/gallery.html', {'photos': photos})
