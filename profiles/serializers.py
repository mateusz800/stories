from rest_framework import serializers
from .models import Profile
from media.serializers import PhotoSerializer

class ProfileSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('name', 'photo')

    def get_name(self, obj):
        return obj.user.get_full_name()

    def get_photo(self, obj):
        serializer = PhotoSerializer(obj.photo, context={'request': self.context['request']})
        return serializer.data