from django.urls import path
from myapp2.views import cw18_1, cw18_2


urlpatterns = [
    path('cw18_1/', cw18_1),
    path('cw18_2/', cw18_2),
]
