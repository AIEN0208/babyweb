from rest_framework import serializers
import album.models as models

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = ('UserId', 'ImageName', 'Image')
