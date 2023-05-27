from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Utilizer,Region,Place,Image,Favorite,Feedback
from .serializers import UtilizerSerializer,MiniPlaceSerializer,PlaceSerializer,ImageSerializer,FavoriteSerializer
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
            return Response("user created",status=201)
        else:
            return Response("error has occured",status=400)
    else:
        return Response("user already exists",status=400)
    
@api_view(['POST'])
def login(request):
    email=request.data["email"]
    password=request.data["password"]
    try:
        query=Utilizer.objects.get(email=email)
        if query :
            if password==query.password:
                serializer=UtilizerSerializer(query)
                return Response(serializer.data)
            else: return Response("incorrect email or password")
    except:
        return Response("incorrect email or password")
    
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
        return Response("success")
    except:
        return Response("non existant admin")
    

@api_view(["GET"])
def getAllPlaceInRegion(request,id):
    query=Place.objects.filter(idRegion=id)
    serializer=MiniPlaceSerializer(query,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getPlace(request,id):
    try:
        placequery=Place.objects.get(id=id)
        if placequery:
            imagequery=Image.objects.filter(idPlace=id)
            imageserializer=ImageSerializer(imagequery,many=True)
            placeserializer=PlaceSerializer(placequery)
            return Response({'data':placeserializer.data,'image':imageserializer.data})
        else: return Response("not found")
    except:
        return Response("not found")

@api_view(["POST"])
def addfavourite(request):
    idUtilizer=request.data["idUtilizer"]
    idPlace=request.data["idPlace"]
    utilizerquery=Utilizer.objects.get(id=idUtilizer)
    placeerquery=Place.objects.get(id=idPlace)
    if placeerquery and utilizerquery:
        fav=Favorite.objects.create(idUtilizer=utilizerquery,idPlace=placeerquery)
        if fav:
            return Response("added to favorites")
        else: return Response("something went wrong try again")
    else: return Response("wrong operation")

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
    return Response(serializer.data)    

    
