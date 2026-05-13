from rest_framework import serializers
from .models import Post, Hashtag


class HashtagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hashtag
    fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
  
  hashtags = HashtagSerializer(many=True, read_only=True, source='hashtag')
  hashtag_names = serializers.ListField(
        child=serializers.CharField(max_length=50),
        write_only=True, #요청에서만 보이고, 응답엔 안보임.
        required=False
    )
  
  
  class Meta:
    model = Post
    fields = (
      'id', 'title', 'date', 'body', 'gender', 'expiration_date', 'open_date', 'hashtags', 'hashtag_names', 'photo'
    )
  def create(self, validated_data):
        # 1. tag_names 데이터 추출 후 validated_data에서 제거
        hashtag_names = validated_data.pop('hashtag_names', [])
        
        # 2. 게시물 먼저 생성
        post = Post.objects.create(**validated_data)
        
        # 3. 태그 저장 및 연결
        for name in hashtag_names:
            # get_or_create를 써서 이미 있는 태그는 가져오고 없으면 생성함
            hashtag, created = Hashtag.objects.get_or_create(name=name)
            post.hashtag.add(hashtag)
            
        return post
  
  def update(self, instance, validated_data):
        # 1. tag_names 데이터 추출
        hashtag_names = validated_data.pop('tag_names', None)
        
        # 2. 기본 필드(title, body 등) 업데이트
        # instance는 수정할 대상 객체입니다.
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # 3. 태그 업데이트 로직
        if hashtag_names is not None:
            # 기존 연결된 태그 관계를 모두 끊음 (태그 객체 자체가 삭제되는 건 아님)
            instance.hashtag.clear()
            
            # 새로 받은 태그 리스트로 다시 연결
            for name in hashtag_names:
                hashtag, created = Hashtag.objects.get_or_create(name=name)
                instance.hashtag.add(hashtag)
                
        return instance
