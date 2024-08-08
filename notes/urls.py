try:
    from django.conf.urls import url , path
except ImportError:
    from django.urls import re_path as url , path



from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notes', NoteViewSet, 'notes')

urlpatterns = [
	path('create_note', create_note, name = 'create_note'),
] + router.urls