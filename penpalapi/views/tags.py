"""View module for handling requests for letter data"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from penpalapi.models import Tag
from django.contrib.auth.models import User


class TagView(ViewSet):
    """Pen Pal API tags view"""

    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """

        # Get 'em outta the database with the Django ORM
        tags = Tag.objects.all()

        # Convert the list to a JSON array
        hunka_tag_serializer = TagSerializer(tags, many=True)

        # Send it all back to the client
        return Response(hunka_tag_serializer.data, status=status.HTTP_200_OK)



    def retrieve(self, request, pk=None):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag record
        """

        # Get it outta the database with the Django ORM
        the_tag = Tag.objects.get(pk=pk)

        # Convert the object to a JSON array
        big_honkin_tag_serializer = TagSerializer(the_tag, many=False)

        # Send it  back to the client
        return Response(big_honkin_tag_serializer.data, status=status.HTTP_200_OK)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'label',)