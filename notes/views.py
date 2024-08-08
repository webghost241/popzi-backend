from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils.open_ai import query_openai
from .models import Note
from .serializers import NoteSerializer
from rest_framework import viewsets, permissions
from problems.views import create_problems
import json

@csrf_exempt
def create_note(request):
	if request.method == 'POST':
		# try:
			content = json.loads(request.body)
			response = query_openai(content['content'])
			note = Note(content=content['content'])
			note.save()
			print(response)
			create_problems(response, note.pk)
			return JsonResponse({'message': 'successful', 'data': {"note_id": note.pk}}, status=200)
		# except:
		# 	return HttpResponse('Something went wrong.', status=400)

class NoteViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.AllowAny]
	queryset = Note.objects.all()
	serializer_class = NoteSerializer