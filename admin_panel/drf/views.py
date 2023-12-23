from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf.models import Teammate
from drf.serializers import TeamSerializer


class TeamListView(APIView):
    def get(self, request):
        queryset = Teammate.objects.all()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)


class GetAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key})
