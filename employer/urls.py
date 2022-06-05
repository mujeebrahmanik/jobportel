from django.urls import path
from employer import views
urlpatterns=[
    path("home",views.Employer_Home_View.as_view(),name='emp-home'),
    path('jobs/add',views.Addjobview.as_view(),name='emp-addjob'),
    path('jobs/all',views.ListJobview.as_view(),name='emp-listjob'),
    path('jobs/detail/<int:id>',views.Jobdetailview.as_view(),name='emp-jobdetail'),
    path('jobs/edit/<int:id>',views.Jobeditview.as_view(),name='emp-editjob'),
    path('jobs/remove/<int:id>',views.Jobdeleteview.as_view(),name='emp-deletejob'),
    path('users/account/signup',views.Signupview.as_view(),name="user-signup"),
    path('users/account/login',views.Loginview.as_view(),name='user-login'),
    path('users/account/logout',views.logout_view,name='user-logout'),
    path('users/account/changepwd',views.Changepwd_view.as_view(),name='changepwd'),
    path('users/account/resetpwd',views.Passwordreset.as_view(),name='pwdreset')
]
