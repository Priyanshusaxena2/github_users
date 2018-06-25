from search.serializers import UserSerializer
from search.utils import get_results_from_api
from rest_framework.views import APIView,Response


class User(APIView):
    """
    API for Searching a single user
    """
    def post(self, request):
        """
        API for getting a user using the username and saving it into the database
        :param request:
        :return: data of the user
        """
        result = get_results_from_api(request.data['username'])
        user_serializer = UserSerializer(data=result)
        if not user_serializer.is_valid():
            return Response({"message": "Failed","error":user_serializer.errors}, status=400)
        user_serializer.save()
        return Response({"message":"success","data":user_serializer.data}, status=200)
    

class UserSearch(APIView):
    """
    
    """
    def get(self,request):
        """
        
        :param request: 
        :return: 
        """
        
        

