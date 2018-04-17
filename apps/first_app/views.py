from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    if 'counter' not in request.session:
      request.session['counter'] = 0
    return render(request, 'first_app/index.html')

def process(request):
  request.session['name'] = request.POST['name']
  request.session['location'] = request.POST['location']
  request.session['language'] = request.POST['language']
  request.session['comment'] = request.POST['comment']

  request.session['counter'] += 1
  return redirect('/results')

def results(request):
  context = {
    'name' : (request.session['name']),
    'location' : (request.session['location']),
    'language' : (request.session['language']),
    'comment' : (request.session['comment']),
  }
  return render(request, 'first_app/results.html', context)
