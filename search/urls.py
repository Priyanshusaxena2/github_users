from django.conf.urls import url, include
from search.views import UserFind,UserSearch

urlpatterns = [
    url(r'^users/', UserFind.as_view()),
    url(r'^users_search/', UserSearch.as_view()),
    

]