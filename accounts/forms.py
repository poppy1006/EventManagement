from django.forms import ModelForm
from .models import Event, Event_Member, Participant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomerForm(ModelForm):
	class Meta:
		model = Participant
		fields = '__all__'
		exclude = ['user']


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class Event_MemberForm(ModelForm):
    class Meta:
        model = Event_Member
        fields = '__all__'


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'phone', 'email']



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
