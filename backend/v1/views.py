from rest_framework.viewsets import ModelViewSet
from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    