"""View module for handling requests for letter data"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db.models import Q
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

        # Check if the query string parameter is there or not
        user = request.query_params.get("user", None) # "author" or "recipient" or None

        # If it is there, check if it is "recipient"
        if user == "either":
            letters = letters.filter(
                Q(author=request.auth.user) |
                Q(recipient=request.auth.user)
            )

        if user == "author":
            letters = letters.filter(author=request.auth.user)

        if user == "recipient":
            letters = letters.filter(recipient=request.auth.user)

        serialized = LetterSerializer(letters, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single letter

        Returns:
            Response -- JSON serialized letter record
        """

        return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request):
        """Handle POST requests for creating a new letter

        Returns:
            Response -- JSON serialized letter record
        """
        recipient = User.objects.get(pk=request.data["recipient"])
        topic = Topic.objects.get(pk=request.data["topic"])


        # new_letter = Letter()
        # new_letter.body=request.data["body"]
        # new_letter.recipient=recipient
        # new_letter.topic=topic
        # new_letter.author=request.auth.user
        # new_letter.save()
        letter = Letter.objects.create(
            body=request.data["body"],
            recipient=recipient,
            topic=topic,
            author=request.auth.user
        )

        serialized = LetterSerializer(letter, many=False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)



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