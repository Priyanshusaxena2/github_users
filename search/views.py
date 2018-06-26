from search.serializers import UserSerializer
from search.utils import get_results_from_api
from rest_framework.views import APIView,Response
from search.models import User

class UserFind(APIView):
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
        return Response({"message": "success","data":user_serializer.data}, status=200)
    

class UserSearch(APIView):
    """
    API for seraching the users according the filters
    Filters can be any field of the User Model
    """
    def get(self, request):
        """
        
        :param request: filter parameters and optional sort variable which decides the order of result
        :return: 
        """
        params = request.query_params.dict()
        sort = 'id'
        if params.get('sort',None):
            sort = params['sort']
            params.pop('sort')
        users = User.objects.filter(**params).order_by(sort)
        user_serializer = UserSerializer(users,many=True)
        return Response({"message": "success","data":user_serializer.data}, status=200)

