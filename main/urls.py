from django.urls import URLPattern, path,include
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('find-counsellor/', views.findcounsellor, name='find-counsellor'),
    path('counsellor-info/', views.counsellorinfo, name='counsellor-info'),
    path('sign-up/', views.signup, name='signup'),
    path('sign-up1/', views.signup1, name='sign-up1'),
    path('sign-up2/', views.signup2, name='sign-up2'),
    path('sign-up3/', views.signup3, name='sign-up3'),
]