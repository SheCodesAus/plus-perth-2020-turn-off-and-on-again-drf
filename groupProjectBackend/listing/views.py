from django.http import Http404
from rest_framework import status, permissions, filters, generics
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Listing, Type, Location, Level, Audience
from .serializers import ListingSerializer
from .serializers import (
    ListingSerializer,
    ListingDetailSerializer,
    TypeSerializer,
    LocationSerializer,
    LevelSerializer,
    AudienceSerializer,
)
from .permissions import IsOwnerOrReadOnly
import json

class ListingList(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ListingSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ["date_created"]
    

    def get_queryset(self):
        queryset = Listing.objects.all()
        typeList = json.loads(self.request.query_params.get('typeList'))
        location = json.loads(self.request.query_params.get('location'))
        audience = json.loads(self.request.query_params.get('audience'))
        level = json.loads(self.request.query_params.get('level'))
        organisation = self.request.query_params.get('organisation')
        if typeList:
            queryset = queryset.filter(typeList__slug=typeList)
        elif location:
            queryset = queryset.filter(location__slug=location)
        elif audience:
            queryset = queryset.filter(audience__slug=audience)
        elif level:
            queryset = queryset.filter(level__slug=level)
        elif organisation:
            queryset = queryset.filter(organisation__slug=organisation)
        return queryset

    def post(self, request):
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListingDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, id):
        try:
            listing = Listing.objects.get(id=id)
            self.check_object_permissions(self.request, listing)
            return listing
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, id):
        listing = self.get_object(id)
        print(listing)
        serializer = ListingDetailSerializer(listing)
        return Response(serializer.data)

    def put(self, request, id):
        listing = self.get_object(id)
        serializer = ListingDetailSerializer(
            instance=listing, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        listing = self.get_object(id)
        listing.delete()
        return Response(status=status.HTTP_200_OK)

class TypeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TypeDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, slug):
        try:
            typeList = Type.objects.get(slug=slug)
            self.check_object_permissions(self.request, typeList)
            return typeList
        except typeList.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        typeList = self.get_object(slug)
        serializer = TypeSerializer(typeList)
        return Response(serializer.data)

    def put(self, request, slug):
        typeList = self.get_object(slug)
        serializer = TypeSerializer(
            instance=typeList, data=request.data, partial=True
        )
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        typeList = self.get_object(slug)
        typeList.delete()
        return Response(status=status.HTTP_200_OK)

class LocationList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, slug):
        try:
            location = Location.objects.get(slug=slug)
            self.check_object_permissions(self.request, location)
            return location
        except location.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        location = self.get_object(slug)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, slug):
        location = self.get_object(slug)
        serializer = LocationSerializer(
            instance=location, data=request.data, partial=True
        )
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        location = self.get_object(slug)
        location.delete()
        return Response(status=status.HTTP_200_OK)

class LevelList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        levels = Level.objects.all()
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LevelDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, slug):
        try:
            level = Level.objects.get(slug=slug)
            self.check_object_permissions(self.request, level)
            return level
        except Level.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        level = self.get_object(slug)
        serializer = LevelSerializer(level)
        return Response(serializer.data)

    def put(self, request, slug):
        level = self.get_object(slug)
        serializer = LevelSerializer(
            instance=level, data=request.data, partial=True
        )
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        level = self.get_object(slug)
        level.delete()
        return Response(status=status.HTTP_200_OK)

class AudienceList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        audiences = Audience.objects.all()
        serializer = AudienceSerializer(audiences, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AudienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AudienceDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, slug):
        try:
            audience = Audience.objects.get(slug=slug)
            self.check_object_permissions(self.request, audience)
            return audience
        except Audience.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        audience = self.get_object(slug)
        serializer = AudienceSerializer(audience)
        return Response(serializer.data)

    def put(self, request, slug):
        audience = self.get_object(slug)
        serializer = AudienceSerializer(
            instance=audience, data=request.data, partial=True
        )
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        audience = self.get_object(slug)
        audience.delete()
        return Response(status=status.HTTP_200_OK)