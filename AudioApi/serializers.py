from .models import AudioBookFields
from rest_framework import serializers


class AudioBookSerializers(serializers.ModelSerializer):
      class Meta:
            model = AudioBookFields
            fields = '__all__'

            extra_kwargs = {
                'ID': {'write_only': True},
                 }
     