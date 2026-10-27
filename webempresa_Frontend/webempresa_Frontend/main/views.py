from django.shortcuts import render

def home(request):
    # Aquí puedes devolver index.html o about.html, dependiendo de cuál sea tu inicio real.
    # En los códigos anteriores vimos que about.html parece ser la historia y hay un index.html
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def store(request):
    return render(request, 'store.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')
