from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Utilizer
from .serializers import UtilizerSerializer,Region
from rest_framework import status

# Create your views here.
@api_view(["GET"])
def index(request):
    Response({"msg":"hello from index"})

@api_view(['POST'])
def register(request):
    email=request.data["email"]
    res=Utilizer.objects.filter(email=email)
    if not res:
        serializer=UtilizerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"created","status":status.HTTP_201_CREATED})
        else:
            return Response({"msg":"error has occured","status":status.HTTP_400_BAD_REQUEST})
    else:
        return Response({"msg":"user already exists","status":status.HTTP_400_BAD_REQUEST})
    
@api_view(['POST'])
def login(request):
    email=request.data["email"]
    password=request.data["password"]
    try:
        query=Utilizer.objects.get(email=email)
        if query :
            if password==query.password:
                serializer=UtilizerSerializer(query)
                return Response({"data":serializer.data,"status":status.HTTP_200_OK})
            else: return Response({"msg":"incorrect email or password","status":status.HTTP_400_BAD_REQUEST})
    except:
        return Response({"msg":"incorrect email or password","status":status.HTTP_400_BAD_REQUEST})
    
@api_view(['POST'])
def addregion(request):
    email=request.data["email"]
    wilaya=request.data["wilaya"]
    latitude=request.data["latitude"]
    longitude=request.data["longitude"]
    try:
        utilizer=Utilizer.objects.get(email=email)
        print(utilizer.id)
        if utilizer :
            addedregion=Region.objects.create(idUser=utilizer,wilaya=wilaya,latitude=latitude,longitude=longitude)
        return Response({"msg":"success","status":status.HTTP_201_CREATED})
    except:
        return Response({"msg":"non existing admin","status":status.HTTP_400_BAD_REQUEST})
