"""Serializers that validate feedback payloads and format feedback API responses."""
from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    """Validate feedback input and keep system-managed fields read-only."""
    student = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        model = Feedback
        fields = '__all__'

        # Safe enhancements with no API shape change.
        read_only_fields = ('created_at', 'status')
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
        }

    def validate(self, data):
        """Normalize feedback text and anonymous routing before saving."""
        # If anonymous is True, student is intentionally not required.
        anonymous = data.get('anonymous', False)
        target = data.get('target')

        if anonymous:
            data['student'] = None

        if isinstance(target, str):
            # Match target values expected by backend role-routing checks.
            data['target'] = target.strip().lower()

        for field in ('subject', 'description'):
            if field in data and isinstance(data[field], str):
                data[field] = data[field].strip()

        return data

FeedbackSerializer.__name__ = 'FeedbackSerializer'
