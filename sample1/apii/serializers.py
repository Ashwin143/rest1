from rest_framework.serializers import serializers


class StudentSerializer(serializers):
    name=serializers.Charfield(max_length=100)
    roll=serializers.IntegerField()
    marks=serializers.IntegerField()

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=model.Article
        fields = '__all__'
