from rest_framework import serializers
from .models import Course

#The below base implemented class just creates a normal searilaizers 

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ('id','name','language','price')


#The below base implemented class just creates a hyperlink searilaizers

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','language','price','url']