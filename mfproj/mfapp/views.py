from rest_framework import viewsets
from rest_framework import permissions

from mfproj.mfapp.models import Peak
from mfproj.mfapp.serializers import PeakSerializer


class PeakViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows peaks to be viewed or edited.
    """
    queryset = Peak.objects.all().order_by('name')
    serializer_class = PeakSerializer
    permission_classes = [permissions.IsAuthenticated]
