from django.urls import path
from .views import home, ContactCreate
from .api import ClientList, ClientDetail, InfoList, InfoDetail, PhoneDetail, PhoneList, ServiceList, ServiceDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', home, name= 'home'),
    path("#contact/", ContactCreate.as_view(), name="contact"),
    #api
    path('client_list/', ClientList.as_view()),
    path('client_detail/<int:pk>/', ClientDetail.as_view()),

    path('info_list/', InfoList.as_view()),
    path('info_detail/<int:pk>/', InfoDetail.as_view()),

    path('phone_list/', PhoneList.as_view()),
    path('phone_detail/<int:pk>/', PhoneDetail.as_view()),
    
    path('service_list/', ServiceList.as_view()),
    path('service_detail/<int:pk>/', ServiceDetail.as_view()),    
]


urlpatterns = format_suffix_patterns(urlpatterns)