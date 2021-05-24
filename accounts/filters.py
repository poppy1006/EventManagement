import django_filters

from .models import *


class Event_memberFilter(django_filters.FilterSet):
    class Meta:
        model = Event_Member
        fields = '__all__'
        exclude = ['participant', 'date_created']

class Event_memberFilter1(django_filters.FilterSet):
    class Meta:
        model = Event_Member
        fields = ['status']

