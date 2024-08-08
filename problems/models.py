import uuid
from django.db import models
from notes.models import Note

class Problem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note = models.ForeignKey(Note, related_name='problems', on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=1000, blank=True, help_text='Enter the answer text', verbose_name='Content')

    @property
    def correct_option(self):
        return self.options.filter(correct=True).first()

    def __str__(self):
        return str(self.content) if self.content else ''  # Return an empty string if content is None

class Option(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    problem = models.ForeignKey(Problem, related_name='options', on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, blank=True, help_text='Enter the answer text', verbose_name='Content')
    explanation = models.CharField(max_length=1000, blank=True, help_text='Enter the explanation text', verbose_name='Explanation')
    correct = models.BooleanField(default=False, help_text='Is this a correct answer?', verbose_name='Correct')

    def __str__(self):
        return self.content or 'No Content'

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
        constraints = [
            models.UniqueConstraint(fields=['problem'], condition=models.Q(correct=True), name='unique_correct_option_for_problem')
        ]