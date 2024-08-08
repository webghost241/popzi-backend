from rest_framework import serializers  
from .models import Problem, Option  # Assuming models is a module in the same Django app  

class CustomOptionSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Option  
        fields = ('id', 'content')  


class OptionSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Option  
        fields = '__all__'  


class ProblemSerializer(serializers.ModelSerializer):  
    # Proper way to specify nested serializers with many=True and read_only=True arguments  
    options = CustomOptionSerializer(many=True, read_only=True)  

    class Meta:  
        model = Problem
        fields = ('id', 'content', 'options')