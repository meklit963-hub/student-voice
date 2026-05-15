"""Notification API views for listing and updating user alerts."""
from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
	"""Allow staff to manage all notifications and users to manage their own."""

	def has_permission(self, request, view):
		return request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		# Staff roles can review notifications across the system.
		if hasattr(request.user, 'role') and request.user.role in ['admin', 'department', 'student_affairs']:
			return True
		# Non-staff users only access notification rows addressed to them.
		return obj.user == request.user


class NotificationViewSet(viewsets.ModelViewSet):
	queryset = Notification.objects.all()
	serializer_class = NotificationSerializer
	permission_classes = [IsOwnerOrAdminOrReadOnly]

	def get_queryset(self):
		user = self.request.user

		if not user.is_authenticated:
			return Notification.objects.none()

		# Safe role access with no logic change.
		role = getattr(user, 'role', None)

		if role in ['admin', 'department', 'student_affairs']:
			return Notification.objects.all()

		return Notification.objects.filter(user=user)

	def perform_create(self, serializer):
		# Safe fallback with no logic change.
		user = self.request.user

		serializer.save(user=user)


# NOTE: removed duplicate unused import (render); safe cleanup only.
