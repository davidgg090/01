from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones import views


class ApiRootVersion2(generics.GenericAPIView):
    name = 'api-root'

    @classmethod
    def get(cls, request, *args, **kwargs):
        return Response({
            'drone-categories': reverse(views.DroneCategoryList.name, request=request),
            'vehicles': reverse(views.DroneList.name, request=request),
            'pilots': reverse(views.PilotList.name, request=request),
            'competitions': reverse(views.CompetitionList.name, request=request)
        })
