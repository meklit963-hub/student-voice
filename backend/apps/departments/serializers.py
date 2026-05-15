"""Serializers that validate and present department data for API consumers."""
from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Serialize department records for staff and mobile clients."""

    class Meta:
        model = Department
        fields = '__all__'

        # Safe enhancement: prevent accidental edits to system fields in updates.
        read_only_fields = ('id', 'created_at')

    # Safe enhancement: improve API output consistency with no database impact.
    def to_representation(self, instance):
        """Trim display-only whitespace before returning department data."""
        data = super().to_representation(instance)

        # Normalize name formatting for UI consistency.
        data['name'] = str(data['name']).strip()

        return data
