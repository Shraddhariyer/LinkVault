from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Link
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_links(request):
    links = Link.objects.all().values()
    return JsonResponse(list(links), safe=False)


@csrf_exempt
def add_link(request):
    if request.method == "POST":
        data = json.loads(request.body)

        url = data.get("url")
        title = data.get("title")
        tag = data.get("tag")

        link = Link.objects.create(
            url=url,
            title=title,
            tag=tag
        )

        return JsonResponse({"message": "Link added successfully"})
@csrf_exempt
def delete_link(request, id):
    if request.method == "DELETE":
        try:
            link = Link.objects.get(id=id)
            link.delete()
            return JsonResponse({"message": "Deleted successfully"})
        except Link.DoesNotExist:
            return JsonResponse({"error": "Link not found"}, status=404)
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "User already exists"}, status=400)

        User.objects.create_user(username=username, password=password)

        return JsonResponse({"message": "User created successfully"})
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)