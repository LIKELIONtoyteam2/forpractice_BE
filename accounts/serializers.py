from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields =(
      'id', 'nickname', 'username', 'email', 'password'
    )
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      nickname=validated_data['nickname']
    )
    user.set_password(validated_data['password'])
    user.save()

    return user
  
class UserLoginSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=100)
  password = serializers.CharField(max_length=128, write_only=True)

  def validate(self, data): #입력받은 데이터 유효성 검사
    username = data.get('username')
    password = data.get('password')

    if User.objects.filter(username=username).exists():
      user = User.objects.get(username=username)

      if not user.check_password(password): #비밀번호 유효성 검사
        raise serializers.ValidationError()
      else:
        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)

        return{
          'id': user.id,
          'username': user.username,
          'email': user.email,
          'access': access,
          'refresh': refresh
        }
      
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nickname', 'profile_image', 'header_image']
        extra_kwargs = {
            'username': {'validators': []},  # unique 검증 제거
        }