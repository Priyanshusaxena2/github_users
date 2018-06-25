from django.conf.urls import url, include
from search.views import User,UserSearch

urlpatterns = [
    url(r'^users/', User.as_view()),
    url(r'^users_search/', UserSearch.as_view()),
    

]