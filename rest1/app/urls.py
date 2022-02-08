# from django.contrib import admin
# # from app import views
# from django.urls import path

# # urlpatterns = [
# #     path('calc/', views.usersApi),
# # ]

# from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from .views import CreateView, DetailsView

# urlpatterns = {
#     url(r'^bucketlists/$', CreateView.as_view()),
#     url(r'^bucketlists/(?P<pk>[0-9]+)/$',
#         DetailsView.as_view()),
# }

# urlpatterns = format_suffix_patterns(urlpatterns)

# def threesquares(m): 
#     if m<0:
#         return False
#     if m==0:
#         return True 
#     for i in range(0,1000):
#         for j in range(0,1000):
#             n=((4**i)*(8*j+7))
#         if(n==m):
#             return False
#         if(n>m):
#             break        
#     return True

# print(threesquares(6))


def hillvalley(l):
    flag=[]
    inc=0
    for i in range(len(l)-1):
        if l[i]<=l[i+1]:
            flag.append(0)
        elif l[i]>=l[i+1]:
            flag.append(1)
    for j in range(len(flag)-1):
        if flag[j]<flag[j+1]:
            inc+=1
        elif flag[j]>flag[j+1]:
            inc+=1
    if inc==1:
        return True
    else:
        return False

print(hillvalley([1,2,3,5,4]))
