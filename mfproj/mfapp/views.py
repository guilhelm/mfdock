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
    # permission_classes = [permissions.IsAuthenticated]


class PeakBoundingBoxViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows peaks to be viewed or edited.
    """

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     lat_min = self.kwargs['lat_min']
    #     lat_max = self.kwargs['lat_max']
    #     lon_min = self.kwargs['lon_min']
    #     lon_max = self.kwargs['lon_max']

    def get_queryset(self):
        return Peak.objects.filter(lat__gte=self.kwargs['lat_min'],
                                   lat__lte=self.kwargs['lat_max'],
                                   lon__gte=self.kwargs['lon_min'],
                                   lon__lte=self.kwargs['lon_max']
                                   ).order_by('name')

    serializer_class = PeakSerializer
    # permission_classes = [permissions.IsAuthenticated]
