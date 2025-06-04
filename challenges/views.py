from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    'january': '[january] Eat no meat for the entire month!',
    'february': '[february] Walk for at least 20 minutes every day!',
    'march': '[march] Learn Django for at least 20 minutes every day',
    'april': '[april] Eat no meat for the entire month!',
    'may': '[may] Eat no meat for the entire month!',
    'june': '[june] Eat no meat for the entire month!',
    'july': '[july] Eat no meat for the entire month!',
    'august': '[august] Eat no meat for the entire month!',
    'september': '[september] Eat no meat for the entire month!',
    'october': '[october] Eat no meat for the entire month!',
    'november': '[november] Eat no meat for the entire month!',
    'december': '[december] Eat no meat for the entire month!'
}


# Create your views here.

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months) or month == 0:
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse(
        'month-challenge', args=[redirect_month])  # /challenge
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound('This month is not supported!')
