from django.shortcuts import render
from .models import Contacts
from django.http import HttpResponse
from .serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
# Create your views here.

############################
# CLASS BASED VIEWS :

class ClassApiView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Contacts.objects.all()
        serializer = ContactSerializer(qs, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DetailView(APIView):
    def get_object(self, id):
        try:
            return Contacts.objects.get(id=id)
        except Contacts.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request, id):
        article = self.get_object(id)
        serializer = ContactSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        contact = self.get_object(id)
        serializer = ContactSerializer(contact,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        contact = self.get_object(id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#################################

# GENERIC VIEWS : 
class GenericApiView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     ):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        
        return self.list(request)

    def post(self,request):
        return self.create(request)

class GenericDetailView(generics.GenericAPIView,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin
                        ):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get(self, request, id):
        
        return self.retrieve(request,id)

    def put(self, request,id):
        return self.update(request,id)

    def delete(self, request ,id):
        return self.destroy(request, id)

##############################
# Generic Viewsets 

class GenericViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()


##################################
# Model Viewsets

class ModelViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()