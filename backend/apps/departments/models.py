"""Department models that represent the offices or units receiving student feedback."""
from django.db import models

class Department(models.Model):
	"""Department or office that can receive routed student feedback."""

	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		# Keep admin lists and API defaults predictable for staff users.
		verbose_name = "Department"
		verbose_name_plural = "Departments"
		ordering = ['name']

	def __str__(self):
		return self.name

	def has_description(self):
		"""Return True when the department has meaningful description text."""
		return bool(self.description and self.description.strip())
