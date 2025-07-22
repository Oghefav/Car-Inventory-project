from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from user.serializer import AdminLoginSerializer, AdminRegisterSerializer, UserSerializer
from user.models import CustomAdminUser
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names= ['get' ]
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        data = CustomAdminUser.objects.all()
        return data
      
class AdminRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = AdminRegisterSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        email = str(serializer.initial_data['email'])
        if CustomAdminUser.objects.filter(email=email).exists():
            return Response({'message' : 'user with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)


        try:
            if serializer.is_valid(raise_exception=True):
               
                user = serializer.save()
                refresh = RefreshToken.for_user(user)

                return Response({
                   'user' : serializer.data,
                   'refresh_token' : str(refresh),
                   'access_token' : str(refresh.access_token),
                   'message' : 'Your account has been successfully'
                }, status=status.HTTP_201_CREATED)


        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
class AdminLoginViewSet(viewsets.ModelViewSet):
    serializer_class = AdminLoginSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            return Response({'data' : validated_data,  'message' : 'you have successfully login in'})