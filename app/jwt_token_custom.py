from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    # Add custom claims
    token['is_staff'] = user.is_staff

    return token

  def validate(self, attrs):
    data = super().validate(attrs)

    # Add extra responses here
    data['is_staff'] = self.user.is_staff

    return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer