"""Serializers that shape notification records for mobile and admin clients."""
from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
	"""Serialize notification records while protecting server-owned timestamps."""

	class Meta:
		model = Notification
		fields = '__all__'

		# Safe enhancements with no API shape change.
		read_only_fields = ('created_at',)
		extra_kwargs = {
			# Clients may omit this when creating an unread notification.
			'is_read': {'required': False},
		}

NotificationSerializer.__name__ = 'NotificationSerializer'
