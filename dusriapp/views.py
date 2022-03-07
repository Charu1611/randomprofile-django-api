from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    apidata = requests.get('https://randomuser.me/api/').json()
    mydata=apidata['results']
    print(mydata)
    return render(request, 'index.html',{'mydata':mydata})
