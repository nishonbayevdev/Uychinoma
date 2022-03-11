from django.shortcuts import render

# Home route
def Home(request):
    return render(request,'index.html',status=200)


# World route
def World(request):
    return render(request,'world.html',status=200)


# Magazine route
def Magazine(request):
    return render(request,'author.html',status=200)


# Blog route
def Blog(request):
    return render(request,'news-post.html',status=200)


# Business route
def Busines(request):
    return render(request,'business.html',status=200)


# Sports route
def Sport(request):
    return render(request,'sports.html',status=200)

# Art route 
def Art(request):
    return render(request,'art.html',status=200)



# Politics route
def Politics(request):
    return render(request,'politics.html',status=200)


# Real-estate 
def RealEstate(request):
    return render(request,'real-estate.html',status=200)


# Travel route
def Travel(request):
    return render(request,'travel.html',status=200)


# About Us route
def AboutUs(request):
    return render(request,'aboutus.html',status=200)


# Contact route
def ContactUs(request):
    return render(request , 'contactus.html',status=200)