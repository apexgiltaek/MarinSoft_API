from django.urls import include, path 
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 두개의 URL을 만들어준다
#router.urls


urlpatterns = [
    path('public/', views.public_post_list),
    path('', include(router.urls)),

]