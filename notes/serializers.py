from rest_framework import serializers
from .models import Note
from problems.serializers import ProblemSerializer
class NoteSerializer(serializers.ModelSerializer):
	problems = ProblemSerializer(many=True, read_only=True)
	class Meta:
		model = Note
		fields = ('id', 'content', 'problems')