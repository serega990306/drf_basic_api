from django.urls import path, include
from . import views
from .views import article_list, article_detail, ArticleAPIview, ArticleDetailAPIview, \
    GenericAPIview, ArticleViewSet, ArticleGenericViewSet, ArticleModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='Article')
router.register('articles', ArticleGenericViewSet, basename='Article')
router.register('articles', ArticleModelViewSet, basename='Article')

urlpatterns = [
    # function based view
    # path('articles/', article_list),
    # path('articles/detail/<int:pk>', article_detail)

    # class based view
    path('articles/', ArticleAPIview.as_view()),
    path('articles/detail/<int:pk>/', ArticleDetailAPIview.as_view()),

    # generics and mixins
    path('generic/articles/<int:pk>/', GenericAPIview.as_view()),

    # viewsets
    path('viewsets/', include(router.urls)),
    path('viewsets/<int:pk>/', include(router.urls)),

    # generic viewsets
    path('gviewsets/', include(router.urls)),
    path('gviewsets/<int:pk>/', include(router.urls)),

    # model viewsets
    path('mviewsets/', include(router.urls)),
    path('mviewsets/<int:pk>/', include(router.urls))
]
