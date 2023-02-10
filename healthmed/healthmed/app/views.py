from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile,VlogPost,Comment,Shorts,Uploadworkoutvideo,Commentworkout,Healthymeals,Blog
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    vlogpost = VlogPost.objects.all()
    return render(request,'index.html',{'vlogpost':vlogpost})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        image = request.FILES['image']
        user = User.objects.create_user(username=username, password=password)
        profile = Profile.objects.create(user=user, profile_picture=image)
        if profile:
            messages.success(request, 'Profile Created Please Login')
            return redirect("loggedin")

    return render(request,'signup.html')

def loggedin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("profile")


    return render(request,'loggedin.html')

def profile(request):
    profile = Profile.objects.get(user=request.user)
    vlogprofile = VlogPost.objects.filter(user=request.user)
    workoutpost= Uploadworkoutvideo.objects.filter(user=request.user)
    return render(request,'profile.html',{'profile':profile,'vlogprofile':vlogprofile,'workoutpost':workoutpost})

def profileworkout(request):
    profile = Profile.objects.get(user=request.user)
    vlogprofile = VlogPost.objects.filter(user=request.user)
    workoutpost= Uploadworkoutvideo.objects.filter(user=request.user)
    workoutfollowers = workoutpost.count()
    print(workoutfollowers)
    return render(request,'profileworkout.html',{'profile':profile,'vlogprofile':vlogprofile,'workoutpost':workoutpost,'workoutfollowers':workoutfollowers})

def profileshorts(request):
    profile = Profile.objects.get(user=request.user)
    shortsprofile = Shorts.objects.filter(user=request.user)
    return render(request,'profileshorts.html',{'shortsprofile':shortsprofile,'profile':profile})

def uploadvlog(request):
    if request.method == 'POST':
        user = request.user
        vlog = request.FILES['vlog']
        mediastram = request.POST['mediastram']
        description = request.POST['description']
        vlogpost = VlogPost(user=user, vlog=vlog, mediastram=mediastram, description=description)
        vlogpost.save()
        if vlogpost:
            redirect('profile')
    return render(request, 'uploadvlog.html')




def edit(request,id):
    profile = Profile.objects.get(id=id)
    if request.method == "POST":
        profiledt = request.FILES["edt"]
        if len(profiledt) !=0:
            profile.profile_picture = profiledt

        profile.save()
    return render(request,'edit.html',{'profile':profile})

def weightraining(request):
    return render(request,'weightraining.html')

def uploadmyworkout(request):
    return render(request,'uploadmyworkout.html')

def uploads(request):
    return render(request,'uploads.html')

def viewvlogs(request,id):
    vlogpost = VlogPost.objects.get(id=id)
    if request.method=='POST':
        comment = request.POST['comment']
        author = request.user
        vlogpost = vlogpost
        vlogcomment = Comment(comment=comment,author=author,vlogpost=vlogpost)
        vlogcomment.save()

    displaycomment = Comment.objects.filter(vlogpost=vlogpost)
    return render(request,'viewvlogs.html',{'vlogpost':vlogpost,'displaycomment':displaycomment})


def Logout(request):
    logout(request)
    return redirect("loggedin")

def shorts(request):
    if request.method == 'POST':
        shorts = request.FILES['shorts']
        user = request.user
        uploadsgorts = Shorts(shorts=shorts,user=user)
        uploadsgorts.save()
    return render(request,'shorts.html')

def like(request,id):
    vlogpost = VlogPost.objects.get(id=id)

    if request.user in vlogpost.likes.all():
        vlogpost.likes.remove(request.user)

    else:
        vlogpost.likes.add(request.user)

    return redirect('index')

def shortslike(request,id):
    shorts = Shorts.objects.get(id=id)

    if request.user in shorts.likes.all():
        shorts.likes.remove(request.user)

    else:
        shorts.likes.add(request.user)

    return render(request,'profileshorts.html')

def uploadworkoutvideo(request):
    if request.method=='POST':
        user = request.user
        video = request.FILES['video']
        titleofvideo = request.POST['titleofvideo']
        dietdescription = request.POST['dietdescription']
        country = request.POST['country']
        day = request.POST['day']
        muscle = request.POST['muscle']
        uploadworkout = Uploadworkoutvideo(user=user,video=video,titleofvideo=titleofvideo,dietdescription=dietdescription
                                    ,country=country,day=day,muscle=muscle)
        uploadworkout.save()

    return render(request,'uploadworkoutvideo.html')

def weightrainning(request):
    weightraining = Uploadworkoutvideo.objects.all()
    return render(request,'weightraining.html',{'weightraining':weightraining})

def workoutcomment(request,id):
    weightraining = Uploadworkoutvideo.objects.get(id=id)
    if request.method == 'POST':
        comment = request.POST['comment']
        author = request.user
        workoutpost = weightraining
        workoutpostcomment = Commentworkout(comment=comment,author=author,workoutpost=workoutpost)
        workoutpostcomment.save()


    displaycomment = Commentworkout.objects.filter(workoutpost=weightraining)
    return render(request,'workoutcomment.html',{'weightraining':weightraining,'displaycomment':displaycomment})

def resturantregistration(request):
    if request.method == 'POST':
        user = request.user
        city = request.POST['city']
        resturantname = request.POST['resturantname']
        whatsappno = request.POST['whatsappno']

        resturantmenu = request.FILES['resturantmenu']

        dishes = Healthymeals(user=user,city=city,resturantname=resturantname,whatsappno=whatsappno,resturantmenu=resturantmenu)
        dishes.save()


    return render(request,'resturantregistration.html')

def navimumbai(request):
    navimumbai = Healthymeals.objects.filter(city='Navimumbai')
    return render(request,'navimumbai.html',{'navimumbai':navimumbai})

def writeblog(request):
    if request.method == 'POST':
        user = request.user
        titleofvideo = request.POST['titleofvideo']
        blogtext = request.POST['blogtext']


        blogimage = request.FILES['blogimage']

        blog = Blog(user=user,titleofvideo=titleofvideo,blogtext=blogtext,blogimage=blogimage)
        blog.save()


    return render(request,'writeblog.html')

def visitmyworkoutyprofile(request,id):
    workoutprofile = Uploadworkoutvideo.objects.get(id=id)
    a =workoutprofile.user
    print(a)
    workprofile = Uploadworkoutvideo.objects.filter(user=a)
    if request.user in workoutprofile.myworkoutfollowers.all():
        workoutprofile.myworkoutfollowers.remove(request.user)

    else:
        workoutprofile.myworkoutfollowers.add(request.user)
    return render(request,'visitmyworkoutyprofile.html',{'workprofile':workprofile,'workoutprofile':workoutprofile})

