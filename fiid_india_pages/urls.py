from django.urls import path
from . import views

app_name = 'fiid-india-pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home-page"),
    path('about/', views.AboutPageView.as_view(), name="about-page"),
    path('about/gallary/', views.about_gallary, name="about-gallary"),
    path('programmes/', views.ProgrammesPageView.as_view(), name="programmes-page"),
    path('programmes/gallary/', views.programmes_gallary,
         name="programmes-gallary"),
    path('objectives/', views.ObjectivesPageView.as_view(), name="objectives-page"),
    path('contact/', views.contact_page_view, name="contact-page"),
    path('files/', views.file_page_view, name="files-page"),
]
