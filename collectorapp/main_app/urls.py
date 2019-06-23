from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gems/', views.gems_index, name='index'),
    path('gems/<int:gem_id>/', views.gems_detail, name='detail'),
    path('gems/create/', views.GemCreate.as_view(), name='gems_create'),
    path('gems/<int:pk>/update', views.GemUpdate.as_view(), name='gems_update'),
    path('gems/<int:pk>/delete', views.GemDelete.as_view(), name='gems_delete'),
    path('gems/<int:gem_id>/add_display', views.add_display, name='add_display'),
    path('gems/<int:gem_id>/assoc_emotion/<int:emotion_id>', views.assoc_emotion, name='assoc_emotion'),
    path('gems/<int:gem_id>/unassoc_emotion/<int:emotion_id>', views.unassoc_emotion, name='unassoc_emotion'),
    path('emotions/', views.EmotionList.as_view(), name='emotion_index'),
    path('emotions/<int:pk>/', views.EmotionDetail.as_view(), name='emotion_detail'),
    path('emotions/create/', views.EmotionCreate.as_view(), name='emotion_create'),
    path('emotions/<int:pk>/update/', views.EmotionUpdate.as_view(), name='emotion_update'),
    path('emotions/<int:pk>/delete/', views.EmotionDelete.as_view(), name='emotion_delete'),
]