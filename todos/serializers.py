from rest_framework import serializers
from todos.models import Todo       # from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # Valores traidos del model
        fields = (
            "id", "title", "body", "created_at",
            "done_at", "updated_at", "deleted_at",
            "status",
        )
        # Valores que no se ven en la api
        read_only_fields = (
            "created_at", "done_at", "updated_at",
            "deleted_at",
        )
