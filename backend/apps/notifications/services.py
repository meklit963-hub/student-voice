"""Service helpers for notification workflows that should stay outside view classes."""
from .models import Notification
from django.db.models import QuerySet
from django.db import transaction
from typing import Optional


def get_all_notifications() -> QuerySet:
	"""Return all notifications with their related user loaded."""
	return Notification.objects.select_related('user').all()


def get_notification_by_id(notification_id: int) -> Optional[Notification]:
	"""Return a notification by ID, or None when it does not exist."""
	try:
		return Notification.objects.select_related('user').get(id=notification_id)
	except Notification.DoesNotExist:
		return None


@transaction.atomic
def create_notification(**kwargs) -> Notification:
	"""Create and return a notification entry."""
	notification = Notification.objects.create(**kwargs)
	return notification


@transaction.atomic
def update_notification(notification_id: int, **kwargs) -> Optional[Notification]:
	"""Update a notification entry and return it, or None if not found."""
	notification = get_notification_by_id(notification_id)
	if notification:
		for key, value in kwargs.items():
			setattr(notification, key, value)
		notification.save()
		return notification
	return None


@transaction.atomic
def delete_notification(notification_id: int) -> bool:
	"""Delete a notification by ID. Returns True when a row was removed."""
	notification = get_notification_by_id(notification_id)
	if notification:
		notification.delete()
		return True
	return False
