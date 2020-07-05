from django.urls import path, include
from . import views
from .views import ClassApiView, DetailView, GenericApiView, GenericDetailView,GenericViewSet # ModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',GenericViewSet, basename='article')
# router.register('model',ModelViewSet,basename='model') for ModelViewSet


urlpatterns = [
    
    path('',ClassApiView.as_view(), name='api'),
    path('detail/<int:id>',DetailView.as_view(), name='detail'),
    
    path('GenericApi',GenericApiView.as_view(),name='generic'),
    path('GenericDetail/<int:id>',GenericDetailView.as_view(), name='GenericDetail'),
    
    path('GViewsets',include(router.urls)),
    path('GViewsets/<int:id>',include(router.urls)),
    # path('MViewsets',include(router.urls)), for ModelViewSet
    # path('GViewsets',GenericViewSet.as_view({'get':'list','post':'create','put':'update'}), name='GViewsets')
   
]
