from django.urls import path
from django.urls import path, include
from . import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('courses/', views.courses, name='courses'),
    path("course/register/<int:course_id>/", views.register_course, name="register_course"),
    path("register/success/", views.register_success, name="register_success"),
    path("gallery/", views.gallery, name="gallery"),
    path('contact/', views.contact_page, name='contact'),
  
    path('login/', views.login_page, name="login"),
    path('signup/', views.signup_page, name="signup"),
    path('forgot-password/', views.CustomPasswordResetView.as_view(), name='forgot_password'),

    path('forgot-password/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('logout/', views.logout_user, name="logout"),

    
]
