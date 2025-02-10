from django.urls import path
from.import views 

urlpatterns = [
    path('',views.homepageview,name="home"),
    path('','about'.aboutpageview,name="about"),
    path('','contact'.contactpageview,name="contact"),
]

