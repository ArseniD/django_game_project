import json
from datetime import datetime

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.exceptions import ValidationError
from django.db.models import Min
from django.db.models import Max

from game_admin import settings
from game_admin.settings import PAGE_SIZE
from models import Players
from models import StatPlayerRegistration
from forms import MailFormFilter
from forms import ExpFormChange
from forms import DateForm



def _login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "login.html", {'redirect_to': next})


def _logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


@login_required
def invalid_input(request):
    return render(request, "invalid_input.html", {})


@login_required
def invalid_login(request):
    return render_to_response('invalid_login.html')


@login_required
def home(request):
    return render(request, "home.html", {})


@login_required
def search_form(request):
    form = MailFormFilter(request.GET)
    players_list = Players.objects.all()
    if form.is_valid():
        players_filter = Players.objects.filter(email=form.cleaned_data['email'])
        return render(request, 'search_form.html', {"form": form, "players_list": players_filter})
    else:
        players_list = Players.objects.all()
        paginator = Paginator(players_list, PAGE_SIZE)
        page = request.GET.get('page')
        try:
            players = paginator.page(page)
        except PageNotAnInteger:
            players = paginator.page(1)
        except EmptyPage:
            players = paginator.page(paginator.num_pages)
        return render(request, 'search_form.html', {"form": form, "players_list": players})


@login_required
def search(request):
    errors = []
    form = MailFormFilter(request.GET)
    if 'email' in request.GET:
        query_email = request.GET['email']
        if not query_email:
            errors.append('Enter a search term - email.')
        elif len(query_email) > 30:
            errors.append('Please enter at most 30 characters.')
        else:
            email_filter = Players.objects.filter(email__icontains=query_email)
            return render(request, 'search_results.html', {"form": form, 'email': email_filter,
                                                           'query_email': query_email})
    return render(request, 'search_results.html', {"form": form, 'errors': errors})


@login_required
def players_change_xp(request, player_id=None):
    form = ExpFormChange(request.GET)
    if request.method == 'GET':
        template_data = {
        "form": form,
        "player": Players.objects.get(id=player_id)
        }
        return render(request, 'players_change_xp.html', template_data)


@login_required
def changed_xp(request, player_id):
    form = ExpFormChange(request.POST)
    player = Players.objects.get(id=player_id)
    template_data = {
            "form": form,
            "player": player,
            }
    if form.is_valid():
        if request.method == 'POST':
            xp = request.POST['xp']
            player.xp += int(xp)
            player.save()
            form = ExpFormChange()
            template_data = {
            "form": form,
            "player": player,
            }
        return render(request, 'players_change_xp.html', template_data)
    return render(request, 'players_change_xp.html', template_data)


@login_required
def stat_players(request):
    stat_player = StatPlayerRegistration.objects.all().order_by('target_date')
    form = DateForm(request.GET)
    paginator = Paginator(stat_player, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(paginator.num_pages)
    return render(request, 'stat_players.html', {"form": form, "stat_players": players})


@login_required
def stat_players_result(request):
    stat_player = StatPlayerRegistration.objects.all().order_by('target_date')
    form = DateForm(request.GET or None)
    try:
        if form.is_valid():
            from_date = form.cleaned_data['fromdate']
            to_date = form.cleaned_data['todate']
            date_min = stat_player.aggregate(Min('target_date'))
            date_max = stat_player.aggregate(Max('target_date'))
            date_min_data = date_min.get('target_date__min')
            date_max_data = date_max.get('target_date__max')
            if from_date is None and to_date < date_min_data:
                return HttpResponseRedirect('/invaild_input/')
            if to_date is None and from_date > date_max_data:
                return HttpResponseRedirect('/invaild_input/')
            if from_date == to_date > date_max_data:
                return HttpResponseRedirect('/invaild_input/')
            if to_date is None:
                stat_player = stat_player.filter(target_date__gte=from_date).order_by('target_date')
                return render(request, 'stat_players_result.html', {"form": form, "stat_players": stat_player})
            if from_date is None:
                stat_player = stat_player.filter(target_date__lte=to_date).order_by('target_date')
                return render(request, 'stat_players_result.html', {"form": form, "stat_players": stat_player})
            if from_date <= to_date > date_min_data:
                stat_player = stat_player.filter(target_date__gte=from_date, target_date__lte=to_date).order_by('target_date')
                return render(request, 'stat_players_result.html', {"form": form, "stat_players": stat_player})
            else:
                return HttpResponseRedirect('/invaild_input/')
        else:
            return HttpResponseRedirect('/invaild_input/')
    except ValueError:
        return HttpResponseRedirect('/invaild_input/')
    except TypeError:
        return HttpResponseRedirect('/stat_players/')






