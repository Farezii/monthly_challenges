from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Try to sleep at least 8 hours a day',
    'february': 'Walk 20 minutes everyday',
    'march': 'do 8 push-ups every day',
    'april': 'kill a man',
    'may': 'kill god',
    'june': 'get a dog',
    'july': 'jumpjacks? idk',
    'august': 'Man youre teally trying huh? go for a jog',
    'september': 'eat a donut',
    'october': 'kill god again',
    'november': 'gaze into the abyss',
    'december': None,
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month.')

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'month': month,
            'text': challenge_text,
        })
    except:
        return HttpResponseNotFound('<h1>Month not supported.</h1>')
