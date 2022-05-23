from rest_framework.viewsets import ModelViewSet

from ..serializers.rack import Rack, RackSerializer


class RackViewSet(ModelViewSet):
    serializer_class = RackSerializer
    queryset = Rack.objects.all()
