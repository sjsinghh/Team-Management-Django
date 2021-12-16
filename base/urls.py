from django.urls import path
from django.urls.resolvers import URLPattern
# from . import views
from .views import TeamCreate, TeamDetail, TeamList, TeamCreate, TeamUpdate, DeleteView

urlpatterns = [
    path('', TeamList.as_view(), name='teamList' ),
    path('team/<int:pk>/', TeamDetail.as_view(), name = 'team'),
    path('team-add/', TeamCreate.as_view(), name='team-add'),
    path('team-update/<int:pk>/', TeamUpdate.as_view(), name='team-update'),
    path('team-delete/<int:pk>/', DeleteView.as_view(), name='team-delete'),

]