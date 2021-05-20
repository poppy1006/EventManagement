from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import EventForm, CreateUserForm , Event_MemberForm, ParticipantForm
from .filters import Event_memberFilter
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    events = Event.objects.all()
    participants = Participant.objects.all()
    event_members = Event_Member.objects.all()

    total_participants = participants.count()
    total_events = events.count()
    completed = events.filter(status='Completed').count()
    upcoming = events.filter(status='Upcoming').count()

    context = {'events': events, 'participants': participants, 'event_members':event_members,'total_participants': total_participants
        , 'total_events': total_events, 'completed': completed, 'upcoming': upcoming}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    events = request.user.participant.event_member_set.all()

    total_events = events.count()
    completed = events.filter(status='Completed').count()
    upcoming = events.filter(status='Upcoming').count()

    context = {'events': events,'total_events': total_events, 'completed': completed, 'upcoming': upcoming}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
def product(request):
    events = Event.objects.all()
    return render(request, 'accounts/profile.html', {'events': events})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    participant = Participant.objects.get(id=pk_test)

    event_members = participant.event_member_set.all()
    event_member_count = event_members.count()

    myFilter = Event_memberFilter(request.GET, queryset=event_members)
    event_members = myFilter.qs
    context = {'participant': participant, 'event_members': event_members, 'event_member_count': event_member_count,
               'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createEvent(request):
    form = EventForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/event_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateEvent(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/event_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect('/')

    context = {'item': event}
    return render(request, 'accounts/delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createEvent_Member(request):
    form = Event_MemberForm()
    if request.method == 'POST':
        form = Event_MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/event_member_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateEvent_Member(request, pk):
    event_member = Event_Member.objects.get(id=pk)
    form = Event_MemberForm(instance=event_member)

    if request.method == 'POST':
        form = Event_MemberForm(request.POST, instance=event_member)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/event_member_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteEvent_Member(request, pk):
    event_member = Event_Member.objects.get(id=pk)
    if request.method == "POST":
        event_member.delete()
        return redirect('/')

    context = {'item': event_member}
    return render(request, 'accounts/delete1.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createParticipant(request):
    form = ParticipantForm()
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/participant_form.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateParticipant(request, pk):
    participant = Participant.objects.get(id=pk)
    form = ParticipantForm(instance=participant)

    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/participant_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteParticipant(request, pk):
    participant = Participant.objects.get(id=pk)
    if request.method == "POST":
        participant.delete()
        return redirect('/')

    context = {'item': participant}
    return render(request, 'accounts/delete2.html', context)






