"""View module for handling requests for topic data"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from penpalapi.models import Topic, Letter


class TopicView(ViewSet):
    """Honey Rae API topics view"""

    def list(self, request):
        """Handle GET requests to get all topics

        Returns:
            Response -- JSON serialized list of topics
        """

        topics = Topic.objects.all()
        serialized = TopicSerializer(topics, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class TopicLetterSerializer(serializers.ModelSerializer):
    """JSON serializer for topics"""

    class Meta:
        model = Letter
        fields = ('id', 'body', 'recipient')


class TopicSerializer(serializers.ModelSerializer):
    """JSON serializer for topics"""
    letters = TopicLetterSerializer(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'label', 'letters',)