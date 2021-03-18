from rest_framework import viewsets
from articles.models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
   

 #from rest_framework.generics import(
      #ListAPIView,
       #RetrieveAPIView,
       #CreateAPIView,
       #UpdateAPIView,
       #DestroyAPIView
       #)
    
#class ArticlesListView(ListAPIView):
     #queryset = Article.objects.all()
     #serializer_class = ArticleSerializer


 #class ArticlesDetailView(RetrieveAPIView):
     #queryset = Article.objects.all()
     #serializer_class = ArticleSerializer

 #class ArticlesCreateView(CreateAPIView):
     #queryset = Article.objects.all()
     #serializer_class = ArticleSerializer

#class ArticlesUpdateView(UpdateAPIView):
    #queryset = Article.objects.all()
     #serializer_class = ArticleSerializer


#class ArticlesDeleteView(DestroyAPIView):
    #queryset = Article.objects.all()
    #serializer_class = ArticleSerializer