""" Platzigram URLs module. """

# Django
from django.contrib import admin
from django.urls import path

# local imports
from platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world', local_views.hello_world),
    path('sorted', local_views.sorted_list),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('post/', posts_views.list_posts)
]