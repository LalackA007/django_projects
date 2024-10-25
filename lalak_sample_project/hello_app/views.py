from django.http import HttpResponse
from django.shortcuts import render

def hello(request, name):
    # return HttpResponse("Name: {}".format(name))
    ctxt = {'name': name}
    return render(request, 'hello_app/hello.html', ctxt)

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


