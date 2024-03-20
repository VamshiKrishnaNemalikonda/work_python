from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("home page requested !!")
    books = ['selfhelp','fantacy','novels']
    #return HttpResponse("<h1>This is home page !!</h1>")
    return JsonResponse(books, safe=False)

