from django.http import HttpResponse, JsonResponse

def home_page(req):
    print("Home page")
    return HttpResponse("<h1>Hello World</h1>")\
    # using JsonResponse we can send the list or some variable in the JSON format

