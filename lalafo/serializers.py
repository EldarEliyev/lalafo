from rest_framework import serializers
from.models.comment import Comment
from.models.elan import Elan
from.models.location import Location
from.models.subcategory import SubCategory

class CommentSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment 
        fields = ["id", "comment",   "like_count"]

    def get_like_count(self, obj):
        return obj.comment_likes.count()

class ElanSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    comment = CommentSerializer(read_only=True) 

    class Meta:
        model = Elan 
        fields = ["id",  "title",  "description",  "comment",  "like_count",  "price"]

    def get_like_count(self, obj):
        return obj.elan_likes.count()
