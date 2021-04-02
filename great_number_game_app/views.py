from django.shortcuts import render, redirect
import random

def index(request):
    if 'attempt_counter' not in request.session:
        request.session['attempt_counter'] = 0
    if 'computer_number' not in request.session:
        request.session['computer_number'] = random.randint(1, 100)
        request.session['too_low'] = False
        request.session['too_high'] = False
        request.session['same_number'] = False
    
    context = {
        'too_low' : request.session['too_low'],
        'too_high' : request.session['too_high'],
        'same_number' : request.session['same_number']
    }    
    return render(request, 'index.html', context)

def guess(request):
    request.session['too_low'] = False
    request.session['too_high'] = False
    request.session['same_number'] = False
    
    # Grab the guess from form and compare
    if (int(request.POST['guess']) < request.session['computer_number']):
        request.session['too_low'] = True
        request.session['attempt_counter'] += 1

    elif (int(request.POST['guess']) > request.session['computer_number']):
        request.session['too_high'] = True
        request.session['attempt_counter'] += 1
    else: 
        request.session['same_number'] = True
        request.session['attempt_counter'] += 1
    # print('>>>>>>>>>>>.', request.session['too_low'], request.session['too_high'], request.session['same_number'], request.session['attempt_counter'])
    return redirect('/')

def destroy_session(request):
    del request.session['attempt_counter']
    request.session.flush()
    return redirect('/')