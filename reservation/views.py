from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Reservation
from .serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['flight_name', 'scheduled', 'depart_from', 'destination']
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # from pdb import set_trace;
        # set_trace()
        serializer.save(created_by=self.request.user)
