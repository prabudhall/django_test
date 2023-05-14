from django.http import HttpResponse, JsonResponse

def home_page(req):
    print("Home page")
    return HttpResponse("<h1>Hello World</h1>")\
    # using JsonResponse we can send the list or some variable in the JSON format

def main_page(req):
    return HttpResponse("<h3>Please add - '/api/items/' in the URL to use the API</h3>"
                        "<h3>Please add - '/admin/' in the URL to visit the admin page where you can see the complete data more clearly</h3>"
                        "<h3>You can also apply condition after the above mentioned URL for only GET request<h3>"
                        "<h3>For PUT and DELETE request you have to add id of the data that you want to update or delete</h3>")