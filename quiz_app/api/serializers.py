from rest_framework import serializers
from quiz_app.models import Quiz, Question
import re


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for question objects."""


    class Meta:
        model = Question
        fields = ["id", "question_title", "question_options", "answer", "created_at", "updated_at"]


class QuizSerializer(serializers.ModelSerializer):
    """Serializer for quiz objects."""


    questions = QuestionSerializer(many=True)


    class Meta:
        model = Quiz
        fields = ["id", "title", "description", "created_at", "updated_at", "video_url", "questions"]


    def validate(self, attrs):
        """Validate the provided attributes."""


        allowed_fields = {"title", "description"}
        for field in attrs: 
            if field not in allowed_fields:
                raise serializers.ValidationError(detail="Only the title and description are can be changed")
        return attrs
     

    def create(self, validated_data):
        """Create and returns a new model instance using the validated data."""


        request = self.context.get("request")
        questions_data = validated_data.pop("questions", [])
        quiz = Quiz.objects.create(owner=request.user, **validated_data)
        for question_data in questions_data:
            Question.objects.create(quiz=quiz, **question_data)
        return quiz
    

    def update(self, instance, validated_data):
        """Update and returns a new model instance using the validated data."""


        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class UrlSerializer(serializers.Serializer):
    """Serializer for urls."""


    url = serializers.URLField()    
    youtube_url_regex = re.compile(r'^https?://(www\.)?youtube\.com/watch\?v=[A-Za-z0-9_-]{11}$')

    
    def validate_url(self, value):
        """Validate the url and raise a error, if the given url is not correct."""


        if not self.youtube_url_regex.match(value):
            raise serializers.ValidationError(detail="Only standard YouTube Urls with 'youtube.com/watch?v=video_id' are allowed.")
        return value