from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from ..models import WatchList,StreamPlatform
from .serializers import WatchListSerializer,StreamPlatformSerializer

class StreamPlatfromAV(APIView):

    def get(self,request):
        streamPlatform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streamPlatform, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlatformSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class StreamPlatformDetailAV(APIView):

    def get(self,request,pk):
        try:
            platform = StreamPlatform.objects.get(pk = pk)
        except:
            return Response({'message': 'Streamplatform doesnot exists.'})
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            platform = StreamPlatform.objects.get(pk = pk)
        except:
            return Response({'message': 'Streamplatform doesnot exists.'})
        serializer = StreamPlatformSerializer(platform, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        try:
            platform = StreamPlatform.objects.get(pk = pk)
        except:
            return Response({'message': 'Streamplatform doesnot exists.'})
        platform.delete()
        return Response({'message':'streamplatform deleted successfully'},status = status.HTTP_204_NO_CONTENT)



class WatchListAV(APIView):
    
    def get(self,request):
        watchLists = WatchList.objects.all()
        serializer = WatchListSerializer(watchLists, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class WatchListDetailAV(APIView):

    # custom function to get movie for given id
    
    def getMovie(self,pk):
        try:
            watchList = WatchList.objects.get(pk = pk)
        except:
            return Response({'error': 'movie for given id doesnot exists.'}, status=status.HTTP_404_NOT_FOUND)
        
        return watchList

    def get(self,request,pk):
        try:
            watchList  = WatchList.objects.get(pk = pk)
        except:
            return Response({'message': 'watchlist doesnot exists.'},status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchList)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            watchList  = WatchList.objects.get(pk = pk)
        except:
            return Response({'message': 'watchlist doesnot exists.'},status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchList, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        try:
            watchList  = WatchList.objects.get(pk = pk)
        except:
            return Response({'message': 'watchlist doesnot exists.'},status=status.HTTP_404_NOT_FOUND)
        watchList.delete()
        return Response({'message': 'movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = WatchListSerializer(movies,many = True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = WatchListSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,movie_id):
#     try:
#         movie = Movie.objects.get(pk = movie_id)
#     except:
#         return Response({'message': 'movie doesnot exists.'},status=status.HTTP_404_NOT_FOUND)
    

#     if request.method == 'GET':
#         serializer = WatchListSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = WatchListSerializer(movie,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)