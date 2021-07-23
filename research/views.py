from .models import Tbl_conference, Tbl_Research, Tbl_chap_based, JournalTb, BookBased, Colaborator
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# ________________________Creating a Conference view sets_____________________________


class ConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ConferenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tbl_conference.objects.filter()

    Tbl_conference.objects.filter(confer_name='Youth connect')



class ResearchViewSet(viewsets.ModelViewSet):
    serializer_class = ResearchSerializer
    permission_classes = [IsAuthenticated]
    queryset = Tbl_Research.objects.all()


class ChapterBasedViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterBasedSerializer
    permission_classes = [IsAuthenticated]
    queryset = Tbl_chap_based.objects.all()


class JournalBasedViewSet(viewsets.ModelViewSet):
    serializer_class = JournalTbSerializer
    permission_classes = [IsAuthenticated]
    queryset = JournalTb.objects.all()


class BookBasedViewSet(viewsets.ModelViewSet):
    serializer_class = BookBasedSerializer
    permission_classes = [IsAuthenticated]
    queryset = BookBased.objects.all()


class ColaboratorViewSet(viewsets.ModelViewSet):
    serializer_class = ColaboratorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Colaborator.objects.all()


class PeerReviewedInternationalView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PeerReviewedInternational.objects.all()
    serializer_class = PeerReviewedInternationalSerializer


class ResearchInnovationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ResearchInnovation.objects.all()
    serializer_class = ResearchInnovationSerializer



    
