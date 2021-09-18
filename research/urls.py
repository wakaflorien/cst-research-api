from django.conf import settings 
from django.conf.urls.static import static  # new

from django.urls import path
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'conference', ConferenceViewSet, basename='conference')
router.register(r'research', ResearchViewSet, basename='research' )

router.register(r'chapter', ChapterBasedViewSet, basename='chapter')
router.register(r'journal', JournalBasedViewSet, basename='journal' )
router.register(r'book', BookBasedViewSet, basename='book')
router.register(r'colaborator', ColaboratorViewSet, basename='colaborator' )
router.register(r'peer', PeerReviewedInternationalView, basename='peer')
router.register(r'innovation', ResearchInnovationView, basename='innovation' )
router.register(r'author', AuthorsViewSet, basename='author' )
router.register(r'community', CommunityViewSet, basename='community' )
router.register(r'mentor', MentorViewSet, basename='mentor' )

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




