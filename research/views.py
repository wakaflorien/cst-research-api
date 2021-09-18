from .models import Tbl_conference, Tbl_Research, Tbl_chap_based, JournalTb, BookBased, Colaborator
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, parsers
from .filter import IsOwnerFilterBackend


# ________________________Creating a Conference view sets_____________________________

class ConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ConferenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tbl_conference.objects.filter(research__staff=user)



class ResearchViewSet(viewsets.ModelViewSet):
    serializer_class = ResearchSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Tbl_Research.objects.all()
    filter_backends = [IsOwnerFilterBackend]

class ChapterBasedViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterBasedSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Tbl_chap_based.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Tbl_chap_based.objects.filter(research__staff=user)
        return queryset


class JournalBasedViewSet(viewsets.ModelViewSet):
    serializer_class = JournalTbSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = JournalTb.objects.filter(research__staff=user)
        return queryset
    


class BookBasedViewSet(viewsets.ModelViewSet):
    serializer_class = BookBasedSerializer
    permission_classes = [IsAuthenticated]
    # queryset = BookBased.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = BookBased.objects.filter(research__staff=user)
        return queryset


class ColaboratorViewSet(viewsets.ModelViewSet):
    serializer_class = ColaboratorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Colaborator.objects.all()
    filter_backends = [IsOwnerFilterBackend]

class CommunityViewSet(viewsets.ModelViewSet):
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticated]
    queryset = Colaborator.objects.all()
    filter_backends = [IsOwnerFilterBackend]


class MentorViewSet(viewsets.ModelViewSet):
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Colaborator.objects.all()
    filter_backends = [IsOwnerFilterBackend]


class AuthorsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorsSerializer
    permission_classes = [IsAuthenticated]
    queryset = Authors.objects.all()



class PeerReviewedInternationalView(viewsets.ModelViewSet):
    serializer_class = PeerReviewedInternationalSerializer
    permission_classes = [IsAuthenticated]
    # queryset = PeerReviewedInternational.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = PeerReviewedInternational.objects.filter(research__staff=user)
        return queryset
    
class ResearchInnovationView(viewsets.ModelViewSet):
    serializer_class = ResearchInnovationSerializer
    permission_classes = [IsAuthenticated]
    # queryset = ResearchInnovation.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = ResearchInnovation.objects.filter(research__staff=user)
        return queryset
    



    
