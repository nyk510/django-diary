from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r"author", views.AuthorViewSet)

urlpatterns = router.urls
