from django.http import HttpResponse
from django.shortcuts import render

def hello(request, name):
    return HttpResponse(f"Hello, {name}!")

def home(request):
    return render(request, 'hello_app/base.html')

def catalog(request):
    return render(request, 'hello_app/catalog.html')

def about(request):
    return render(request, 'hello_app/about.html')


def calc(request, a, b):
    return HttpResponse("{}+{}={}".format(a, b, a+b))

def getuser(request):
    name = request.GET['name']
    return HttpResponse("Name: {}".format(name))



def cookie(request):
    response = HttpResponse(content_type='text/html')
    response.set_cookie('author', 'Lalak')

    if 'page_views' in request.session:
        request.session['page_views'] += 1
    else:
        request.session['page_views'] = 1

    cookies = request.COOKIES

    html = '''
    <html>
    <body>
        <h2>Cookies:</h2>
        <ul>
    '''

    if cookies:
        for key, value in cookies.items():
            html += f"<li><strong>{key}:</strong> {value}</li>"
    else:
        html += "<li>No cookies available.</li>"

    html += f'''
        </ul>
        <h2>Page Views: {request.session['page_views']}</h2>
    </body>
    </html>
    '''

    response.content = html
    return response


