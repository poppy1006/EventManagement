from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),
    path('user/', views.userPage, name="user-page"),
    path('events/', views.product, name='events'),
    path('participant/<str:pk_test>/', views.customer, name='participant'),

    path('create_event/', views.createEvent, name='create_event'),
    path('update_event/<str:pk>/', views.updateEvent, name='update_event'),
    path('delete_event/<str:pk>/', views.deleteEvent, name='delete_event'),

    path('create_event_member/', views.createEvent_Member, name='create_event_member'),
    path('update_event_member/<str:pk>/', views.updateEvent_Member, name='update_event_member'),
    path('delete_event_member/<str:pk>/', views.deleteEvent_Member, name='delete_event_member'),


    path('create_participant/', views.createParticipant, name='create_participant'),
    path('update_participant/<str:pk>/', views.updateParticipant, name='update_participant'),
    path('delete_participant/<str:pk>/', views.deleteParticipant, name='delete_participant'),
]
