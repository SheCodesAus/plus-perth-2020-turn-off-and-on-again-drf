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
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganisationDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, slug):
        try:
            organisation = Organisation.objects.get(slug=slug)
            self.check_object_permissions(self.request, organisation)
            return organisation
        except Organisation.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        organisation = self.get_object(slug)
        serializer = OrganisationDetailSerializer(organisation)
        return Response(serializer.data)

    def put(self, request, slug):
        organisation = self.get_object(slug)
        serializer = OrganisationDetailSerializer(
            instance=organisation, data=request.data, partial=True
        )
        if serializer.is_valslug():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        organisation = self.get_object(slug)
        organisation.delete()
        return Response(status=status.HTTP_200_OK)


