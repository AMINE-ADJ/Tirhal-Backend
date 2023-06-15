from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Utilizer,Place,Region,Image,Favorite,Comment,Rating,Transport,Event
from .serializers import UtilizerSerializer,RegionSerializer,PlaceSerializer,MiniPlaceSerializer,ImageSerializer,FavoriteSerializer,CommentSerializer,RatingSerializerOnadd,CommentSerializerOnadd,RatingSerializer,TransportSerializer
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
            transportquery=Transport.objects.filter(idPlace=id)
            transportserializer=TransportSerializer(transportquery,many=True)
            imageserializer=ImageSerializer(imagequery,many=True)
            placeserializer=PlaceSerializer(placequery)
            return Response({'data':placeserializer.data,'image':imageserializer.data,'transport':transportserializer.data,"status":status.HTTP_200_OK})
        else: return Response({"data":"not found","status":status.HTTP_404_NOT_FOUND})
    except:
        return Response({"data":"not found","status":status.HTTP_404_NOT_FOUND})

@api_view(["POST"])
def SearchPlaces(request,id):
    param=request.data
    query1=Place.objects.filter(category__icontains=param["category"],theme__icontains=param["theme"],name__icontains=param["name"],idRegion=id)
    serializer=MiniPlaceSerializer(query1,many=True)
    return Response({"data":serializer.data,"status":status.HTTP_200_OK})

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
def getcomments(request,id):
    query=Comment.objects.filter(idPlace=id)
    serializer=CommentSerializer(query,many=True)
    query1=Rating.objects.filter(idPlace=id)
    serializer1=RatingSerializer(query1,many=True)
    return Response({"data":serializer.data,"rating":serializer1.data,"status":status.HTTP_200_OK})


@api_view(["GET"])
def gettotalrating(request,id):
    query=Rating.objects.filter(idPlace=id)
    average=0
    count=query.count()
    for element in query:
        average=element.value+average
    average=average/count
    return Response({"data":average,"status":status.HTTP_200_OK})



# @api_view(["POST"])
# def getrating(request,id):
#     param=request.data
#     query=Rating.objects.filter(idPlace=id,idUtilizer=int(param["idUtilizer"]))
#     serializer=RatingSerializer(query,many=True)
#     return Response({"data":serializer.data,"status":status.HTTP_200_OK})


@api_view(["POST"])
def addcomment(request):
    # idplace=int(request.data["idPlace"])
    # idutilizer=int(request.data["idUtilizer"])
    # Comment=float(request.data["comment"])
    serializer=CommentSerializerOnadd(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"comment added successfully","status":status.HTTP_201_CREATED})
    else: return Response({"msg":"something went wrong","status":status.HTTP_400_BAD_REQUEST})


@api_view(["POST"])
def addrating(request):
    serializer=RatingSerializerOnadd(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"rating added successfully","status":status.HTTP_201_CREATED})
    else: return Response({"msg":"something went wrong","status":status.HTTP_400_BAD_REQUEST})



