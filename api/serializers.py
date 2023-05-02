from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    rollNo = serializers.IntegerField()
    address = serializers.CharField(max_length = 100)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.rollNo = validated_data.get('rollNo',instance.rollNo)
        instance.address = validated_data.get('address',instance.address)
        instance.save()
        return instance 