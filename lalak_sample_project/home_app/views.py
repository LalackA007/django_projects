from django.http import HttpResponse
import html
import random
from django.middleware.csrf import get_token


def home(request):
    content = '''<h1>Home page<h1>
    <ul>
        <li><a href='/hello/Sofia'>Hello</a></li>
        <li><a href='/calc/6/9'>Calc</a></li>
        <li><a href='/showgame'>Guess the Number Game</a></li>
    </ul>'''

    return HttpResponse(content)


def dumpdata(place, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval
    

def showgame(request):
    if request.method == 'GET':
        n = random.randint(1, 100)
        request.session['number'] = n 

        token = get_token(request)

        response = f"""
            <p>Impossible Guessing Game</p>
            <form action="/showgame/" method="POST">
            <p>
              <label for="guess">Input Guess</label>
              <input type="text" name="guess" size="40" id="guess"/>
              <input type="hidden" name="csrfmiddlewaretoken" value="{html.escape(token)}"/>
            </p>
              <input type="submit" value="Submit Guess"/>
            </form>"""

        return HttpResponse(response)

    elif request.method == 'POST':
        n = request.session.get('number', None)

        if n is None:
            return HttpResponse("The game session has expired. Please start a new game.")

        guess = request.POST.get('guess')
        if guess is None:
            p = 'Please enter a number'
        else:
            try:
                guess = int(guess)
                if guess == n:
                    p = 'Congratulations! You guessed it right!'
                elif guess < n:
                    p = 'Guess again! Number is higher.'
                else:
                    p = 'Guess again! Number is lower.'
            except ValueError:
                p = 'Please enter a valid number.'

        csrf_token = get_token(request)
        content = f"""
            <p>Impossible Guessing Game</p>
            <form action="/showgame/" method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" value="{html.escape(csrf_token)}"/>
            <p>
              <label for="guess">Input Guess</label>
              <input type="text" name="guess" size="40" id="guess"/>
            </p>
              <input type="submit" value="Submit Guess"/>
            </form>
            <p>{p}</p>"""

        return HttpResponse(content)
