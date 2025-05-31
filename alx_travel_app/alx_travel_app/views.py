from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to Blandine's Travel App!</h1><p>The server is running!</p>")
