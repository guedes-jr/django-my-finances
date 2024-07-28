from django.shortcuts import render

def dashboard(request):
    return render(request, 'home.html')

def buttons(request):
    return render(request, 'ui-features/buttons.html')

def dropdowns(request):
    return render(request, 'ui-features/dropdowns.html')

def typography(request):
    return render(request, 'ui-features/typography.html')

def forms(request):
    return render(request, 'forms/basic_elements.html')

def tables(request):
    return render(request, 'tables/basic-table.html')

def charts(request):
    return render(request, 'charts/chartjs.html')

def icons(request):
    return render(request, 'icons/font-awesome.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def not_found(request):
    return render(request, 'error-404.html')

def internal_server_error(request):
    return render(request, 'error-500.html')

def blankpage(request):
    return render(request, 'blank-page.html')

def documentation(request):
    return render(request, 'docs/documentation.html')
