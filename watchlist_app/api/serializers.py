from rest_framework import serializers
from ..models import WatchList,StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchList
        fields = "__all__"





# class MovieSerializer(serializers.ModelSerializer):
    
#     len_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = "__all__"
#         # fields = ['id','name','description','active',]
#         # exclude = ['active']

#     # custom serialization field
#     def get_len_name(self,object):
#         length = len(object.name)
#         return length
    

#        # object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and description must be different")
#         else:
#             return data
        

#     #     # field level validation
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name must be more than two character.")
#         else:
#             return value

# # validation using validators
# def name_length(value):
#     if len(value)< 2:
#         raise serializers.ValidationError("Name must be more than two character.")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
 
    

