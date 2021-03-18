from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',ArticleViewSet, basename='articles')
urlpatterns = router.urls





#from django.urls import path

#from .views import ArticlesListView, ArticlesDetailView

#urlpatterns = [
    #path('', ArticlesListView.as_view(), name=" ArticlesDetailView"),
    #path("create/", ArticlesCreateView.as_view(), name="ArticlesDetailView"),
    #path("<pk>",  ArticlesDetailView.as_view(), name="ArticleCreateView "),
    #path("<pk>/update/", ArticlesUpdateView.as_view(), name="ArticlesUpdateView "),
    #path("<pk>/delete",  ArticlesDeleteView.as_view(), name="ArticlesDeleteView"),
#]
