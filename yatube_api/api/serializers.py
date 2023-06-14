from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'pub_date',
            'author',
            'image',
            'group',
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'author',
            'post',
            'created',
        )
        read_only_fields = ('post',)

    def get_post(self, obj):
        return obj.post.pk
