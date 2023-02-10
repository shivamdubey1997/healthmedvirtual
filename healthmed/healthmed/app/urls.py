from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('loggedin/',views.loggedin,name="loggedin"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.Logout,name="logout"),
    path('uploadvlog/',views.uploadvlog,name="uploadvlog"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('weightraining/',views.weightraining,name="weightraining"),
    path('uploadmyworkout/',views.uploadmyworkout,name="uploadmyworkout"),
    path('uploads/',views.uploads,name="uploads"),
    path('viewvlogs/<int:id>/',views.viewvlogs,name="viewvlogs"),
    path('shorts/',views.shorts,name="shorts"),
    path('like/<int:id>/',views.like,name="like"),
    path('profileshorts/',views.profileshorts,name="profileshorts"),
    path('shortslike/',views.shortslike,name="shortslike"),
    path('weightrainning/',views.weightrainning,name="weightrainning"),
    path('uploadworkoutvideo/',views.uploadworkoutvideo,name="uploadworkoutvideo"),
    path('workoutcomment/<int:id>/',views.workoutcomment,name="workoutcomment"),
    path('resturantregistration/',views.resturantregistration,name="resturantregistration"),
    path('navimumbai/',views.navimumbai,name="navimumbai"),
    path('writeblog/',views.writeblog,name="writeblog"),
    path('profileworkout/',views.profileworkout,name="profileworkout"),
    path('visitmyworkoutyprofile/<int:id>/',views.visitmyworkoutyprofile,name="visitmyworkoutyprofile"),

]