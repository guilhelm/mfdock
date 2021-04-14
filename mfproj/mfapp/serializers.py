from rest_framework import serializers
from mfproj.mfapp.models import Peak


class PeakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peak
        fields = ['name', 'lat', 'lon', 'altitude']
