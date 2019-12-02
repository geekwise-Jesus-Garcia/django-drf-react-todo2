from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        modle = Todo
        fields = ('id', 'title', 'description', 'completed')