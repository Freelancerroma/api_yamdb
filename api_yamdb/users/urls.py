from django.urls import include, path
from rest_framework import routers

from users.views import (APIAuthSignup, 
                         APIAuthToken, 
                         APIUserDetail, 
                         APIUserMe,
                         UserViewSet)

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/users/me/', APIUserMe.as_view()),
    path('v1/users/<str:username>/', APIUserDetail.as_view()),
    path('v1/auth/signup/', APIAuthSignup.as_view()),
    path('v1/auth/token/', APIAuthToken.as_view()),
]
