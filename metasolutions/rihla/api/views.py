from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Utilizer,Place,Region,Image,Favorite,Feedback
from .serializers import UtilizerSerializer,RegionSerializer,PlaceSerializer,MiniPlaceSerializer,ImageSerializer,FavoriteSerializer,FeedbackSerializer,FeedbackSerializerOnadd
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

    

@api_view(["GET"])
def getAllPlaceInRegion(request,id):
    query=Place.objects.filter(idRegion=id)
    serializer=MiniPlaceSerializer(query,many=True)
    return Response({"data":serializer.data,"status":status.HTTP_200_OK})

@api_view(["GET"])
def getPlace(request,id):
    try:
        placequery=Place.objects.get(id=id)
        if placequery:
            imagequery=Image.objects.filter(idPlace=id)
            imageserializer=ImageSerializer(imagequery,many=True)
            placeserializer=PlaceSerializer(placequery)
            return Response({'data':placeserializer.data,'image':imageserializer.data,"status":status.HTTP_200_OK})
        else: return Response({"data":"not found","status":status.HTTP_404_NOT_FOUND})
    except:
        return Response({"data":"not found","status":status.HTTP_404_NOT_FOUND})

@api_view(["POST"])
def addfavourite(request):
    idUtilizer=request.data["idUtilizer"]
    idPlace=request.data["idPlace"]
    utilizerquery=Utilizer.objects.get(id=idUtilizer)
    placeerquery=Place.objects.get(id=idPlace)
    if placeerquery and utilizerquery:
        fav=Favorite.objects.create(idUtilizer=utilizerquery,idPlace=placeerquery)
        if fav:
            return Response({"msg":"added to favorites","status":status.HTTP_201_CREATED})
        else: return Response({"msg":"something went wrong try again","status":status.HTTP_400_BAD_REQUEST})
    else: return Response({"msg":"wrong operation","status":status.HTTP_401_UNAUTHORIZED})

@api_view(["GET"])
def getfavorite(request,id):
    placelist=[]
    query=Favorite.objects.filter(idUtilizer=id)
    favoriteserilizer=FavoriteSerializer(query, many=True)
    idplace=favoriteserilizer.data[1]["idPlace"]
    i=0
    for element in query:
        idplace=favoriteserilizer.data[i]["idPlace"]
        placelist.extend(list(Place.objects.filter(id=idplace)))
        i=i+1
    print(placelist)
    serializer=PlaceSerializer(placelist,many=True)
    return Response({"data":serializer.data})    

@api_view(["GET"])
def getfeedbacks(request,id):
    query=Feedback.objects.filter(idPlace=id)
    serializer=FeedbackSerializer(query,many=True)
    return Response({"data":serializer.data,"status":status.HTTP_200_OK})

# @api_view(["POST"])
# def addfeedback(request):
#     idplace=int(request.data["idPlace"])
#     idutilizer=int(request.data["idUtilizer"])
#     rating=float(request.data["rating"])

