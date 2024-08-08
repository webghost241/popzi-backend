import uuid

from django.db import models


class Note(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	content = models.CharField(max_length=10000,
	                           blank=False,
	                           help_text=("Enter the content text"),
	                           verbose_name=("Content"))

	@property
	def get_problems(self):
		return self.problems.all()

	@property
	def save_problems(self):
		pass
