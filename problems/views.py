from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import ProblemSerializer, OptionSerializer  # Ensure correct relative import
from .models import Problem, Option  # Ensure correct relative import
from utils.split_question import extract_info, split_options, split_index


class ProblemViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.AllowAny]
	queryset = Problem.objects.all()
	serializer_class = ProblemSerializer


class OptionViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.AllowAny]
	queryset = Option.objects.all()
	serializer_class = OptionSerializer

	def list(self, request, *args, **kwargs):
		# Corrected to properly return a 405 Method Not Allowed response.
		return Response({'message': 'Listing of objects is not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def create_problems(content, note_id):
	questions = extract_info(content, 'QUESTIONSTART', 'QUESTIONEND')
	correct_answers = extract_info(content, 'CORRECTANSWERSTART', 'CORRECTANSWEREND')
	explanations = extract_info(content, 'EXPLANATIONSTART', 'EXPLANATIONEND')
	why_wrong = extract_info(content, 'WHYWRONGSTART', 'WHYWRONGEND')



	for index, question in enumerate(questions):
		q_text, options = split_options(question)
		problem = Problem(content=q_text, note_id=note_id)  # Updated for correct object creation
		problem.save()
		create_options(options, correct_answers[index], explanations[index], why_wrong[index], problem.pk)


def create_options(options, correct_answer, explanation, why_wrong, problem_id):
	correct_answer = split_index(correct_answer)
	options = [option.strip() for option in options]
	correct_index = options.index(correct_answer)
	options[correct_index] = Option(content=correct_answer, explanation=explanation, correct=True, problem_id=problem_id)  # Setting the correct option text
	why_wrong = why_wrong.split('\n')

	wrong_index = 0
	for index, option in enumerate(options):
		if index != correct_index:
			options[index] = Option(content=options[index],
			                        explanation=split_index(why_wrong[wrong_index]),
			                        correct=False,
			                        problem_id=problem_id)
			wrong_index = wrong_index + 1

	for option in options:
		option.save()