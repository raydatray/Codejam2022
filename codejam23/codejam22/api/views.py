from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import listing, User
from .serializers import listingSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


# Create your views here.


@api_view(["GET"])
def getListing(request, id):
    if id == "all":
        listings = listing.objects.all()
        serializer = listingSerializer(listings, many=True)
    else:
        id = int(id)
        listings = listing.objects.get(pk=id)
        serializer = listingSerializer(listings)
    return Response(serializer.data)


@api_view(["POST"])
def createListing(request):
    listing = listingSerializer(data=request.data)
    if listing.is_valid():
        listing.save()

    return Response({"Status": "got it"}, status=status.HTTP_200_OK)


@api_view(["PUT"])
def updateListing(request, id):
    id = int(id)
    Listing = listing.objects.get(pk=id)
    serializer = listingSerializer(Listing, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status": "got it"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def deleteListing(request, id):
    id = int(id)
    Listing = listing.objects.get(pk=id)
    Listing.delete()
    return Response({"Status": "got it"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def sendRequest(request):
    requestUser = User.objects.get(pk=request.GET["otherUserSessionId"])
    current = User.objects.get(pk=request.GET["currentUser"])
    current.request.add(requestUser)
    return HttpResponse("all good")
