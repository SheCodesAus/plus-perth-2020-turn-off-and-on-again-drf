from django.http import Http404
from rest_framework import status, permissions, filters, generics
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Organisation
from .serializers import (
    OrganisationSerializer,
    OrganisationDetailSerializer,
)
from .permissions import IsOwnerOrReadOnly

class OrganisationList(ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrganisationSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ["date_created"]

    def get_queryset(self):
        queryset = Organisation.objects.all()
        return queryset

    def post(self, request):
        serializer = OrganisationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganisationDetail(APIView):
    permission_classes = []

    def get_object(self, id):
        try:
            organisation = Organisation.objects.get(id=id)
            self.check_object_permissions(self.request, organisation)
            return organisation
        except Organisation.DoesNotExist:
            raise Http404

    def get(self, request, id):
        organisation = self.get_object(id)
        print(organisation)
        serializer = OrganisationDetailSerializer(organisation)
        return Response(serializer.data)

    def put(self, request, id):
        organisation = self.get_object(id)
        serializer = OrganisationDetailSerializer(
            instance=organisation, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        organisation = self.get_object(id)
        organisation.delete()
        return Response(status=status.HTTP_200_OK)


