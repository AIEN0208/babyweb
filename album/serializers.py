from rest_framework import serializers
import album.models as models

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = ('UserId', 'ImageName', 'Image')

class PaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paint
        fields = ('UserId', 'ImageName', 'Image')

class CoveredSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Covered
        fields = ('UserId', 'ImageName', 'Image')