from django.conf.urls import url
from django.urls import path
from .views import * 
from rest_framework.routers import DefaultRouter

journal_list = JournalBasedViewSet.as_view({'get': 'list','post': 'create',})
journal_detail = JournalBasedViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy',})
book_list = BookBasedViewSet.as_view({'get': 'list','post': 'create',})
book_detail = BookBasedViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy',})
colaborators_list = ColaboratorViewSet.as_view({'get': 'list','post': 'create',})
colaborator_detail = ColaboratorViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy',})

chapter_list = ChapterBasedViewSet.as_view({'get': 'list','post': 'create',})
chapter_detail = ChapterBasedViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy',})
research_list = ResearchViewSet.as_view({'get': 'list','post': 'create',})
research_detail = ResearchViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy',})
conference_list = ConferenceViewSet.as_view({'get': 'list','post': 'create',})
conference_detail = ConferenceViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy',})
urlpatterns = ([
   
    path('journal_list/', journal_list, name='journal_list'),
    path('journal_detail/<int:pk>/', journal_detail, name = 'journal_detail'),
    path('book_list/', book_list, name = 'book_list'),
    path('book_detail/<int:pk>/', book_detail, name = 'book_detail'),
    path('colaborators/', colaborators_list, name = 'colaborator_list'),
    path('colaborators/<int:pk>/', colaborator_detail, name = 'colaborator_detail'),

    path('researches/', research_list, name = 'research_list'),
    path('researches/<int:pk>/', research_detail, name = 'research_detail'),
    path('chapter_based/', chapter_list, name = 'chapter_list'),
    path('chapter_based/<int:pk>/', chapter_detail, name = 'chapter_detail'),
    path('conferences/', conference_list, name = 'conference_list'),
    path('conferences/<int:pk>/', conference_detail, name = 'conference_detail')
])




