from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),
    path('user/', views.userPage, name="user-page"),

    path('account/', views.accountSettings, name="account"),

    path('events/', views.product, name='events'),
    path('eventss/', views.eventss, name='eventss'),
    path('participants/', views.participant, name='participants'),
    path('participantss/', views.participantss, name='participantss'),
    path('event_member/', views.event_member, name='event_member'),
    path('participant/<str:pk_test>/', views.customer, name='participant'),
    path('event/<str:pk>/', views.event, name='event'),

    path('create_event/', views.createEvent, name='create_event'),
    path('update_event/<str:pk>/', views.updateEvent, name='update_event'),
    path('delete_event/<str:pk>/', views.deleteEvent, name='delete_event'),

    path('create_event_member/<str:pk>/', views.createEvent_Member, name='create_event_member'),
    path('update_event_member/<str:pk>/', views.updateEvent_Member, name='update_event_member'),
    path('delete_event_member/<str:pk>/', views.deleteEvent_Member, name='delete_event_member'),

    path('create_participant/', views.createParticipant, name='create_participant'),
    path('update_participant/<str:pk>/', views.updateParticipant, name='update_participant'),
    path('delete_participant/<str:pk>/', views.deleteParticipant, name='delete_participant'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),

]
