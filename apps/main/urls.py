# Path of django
from django.urls import path,re_path
# Routes
from .views import Home
from .views import World
from .views import  Magazine
from .views import Blog
from .views import Busines
from .views import Sport
from .views import Art
from .views import Politics
from .views import RealEstate
from .views import Travel
from .views import ContactUs
from .views import AboutUs

# Paths


urlpatterns = [
    # Home route start
    path('' , Home , name = 'home'),



    # Home route end


    # World route start
    path('world/' , World , name = 'world'),



    # World route end

    # Magaine route start 
    path('magazine/' , Magazine , name = 'magazine'),



    # Magazine route end

    # Blog route start
    path('blog/' , Blog , name = 'blog'),


    # Blog route end 

    # Business route start
    
    path('business/' , Busines , name = 'business'),

    
    # Business route end

    # Sport route start

    path('sport/' , Sport , name = 'sport'),


    # Sport route end

    # Art route start 

    path('art/' , Art , name = 'art'),


    # Art route end

    # Politics route start

    path('politics/' , Politics , name = 'politics'),


    # Politics route end

    # Real-Estate route start

    path('real-estate/' , RealEstate , name = 'real-estate'),


    # Real-Estate route end

    # Travel route start

    path('travel/' , Travel , name = 'travel'),


    # Travel route end


    # Contact route start\

    path('contact/' , ContactUs , name = 'contact'),


    # Contact route end


    # About Us route start 
    path('about/' , AboutUs , name = 'about'),



    # About Us route end
]