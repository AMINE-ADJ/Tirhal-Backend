from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Utilizer
from .serializers import UtilizerSerializer

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
        Response("user already exists",status=400)
