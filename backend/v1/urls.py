from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('articles', views.ArticleViewSet)
router.register("author", views.AuthorViewSet)

urlpatterns = router.urls
