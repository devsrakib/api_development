from rest_framework import serializers

from myapp.models import Contact


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=100)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    email = serializers.EmailField(max_length=30)

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            "name",
        )
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        return instance
