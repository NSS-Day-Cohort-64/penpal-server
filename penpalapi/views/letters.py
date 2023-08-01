"""View module for handling requests for letter data"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from penpalapi.models import Letter, Topic
from django.contrib.auth.models import User


class LetterView(ViewSet):
    """Honey Rae API letters view"""

    def list(self, request):
        """Handle GET requests to get all letters

        Returns:
            Response -- JSON serialized list of letters
        """

        letters = Letter.objects.all()
        serialized = LetterSerializer(letters, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single letter

        Returns:
            Response -- JSON serialized letter record
        """

        return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', )

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'label', )

class LetterSerializer(serializers.ModelSerializer):
    """JSON serializer for letters"""
    topic = TopicSerializer(many=False)
    author = UserSerializer(many=False)
    recipient = UserSerializer(many=False)

    class Meta:
        model = Letter
        fields = ('id', 'author', 'recipient', 'body', 'date_created', 'topic')