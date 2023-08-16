"""View module for handling requests for letter data"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User


class RecipientView(ViewSet):
    """Pen Pal API recipients view"""

    def list(self, request):
        """Handle GET requests to get all recipients

        Returns:
            Response -- JSON serialized list of recipients
        """

        # Get 'em outta the database with the Django ORM
        recipients = User.objects.exclude(username=request.auth.user.username)

        # Convert the list to a JSON array
        ubër_user_serializer = RecipientSerializer(recipients, many=True)

        # Send it all back to the client
        return Response(ubër_user_serializer.data, status=status.HTTP_200_OK)



class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', )