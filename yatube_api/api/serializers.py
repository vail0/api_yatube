# kittygram/cats/serializers.py

from rest_framework import serializers

from posts.models import Comment, Group, Post, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )
    # aurhor = serializers.StringRelatedField(
    #     slug_field='username',
    #     read_only=True,
    # )
    publication_date = serializers.DateTimeField(
        read_only=True,
        source='pub_date'
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'publication_date', 'author', 'image', 'group')
        # укажите поля, доступные только для чтения
        # read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    # post = serializers.PrimaryKeyRelatedField(read_only=True)
    # aurhor = serializers.StringRelatedField(
    #     slug_field='username',
    #     read_only=True,
    # )
    creation_date = serializers.DateTimeField(
        read_only=True,
        source='created'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'creation_date')
