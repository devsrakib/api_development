from rest_framework import serializers

from myapp.models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="contact-list", read_only=True
    )

    class Meta:
        model = Contact
        fields = ["url", "id", "name", "title", "email"]
