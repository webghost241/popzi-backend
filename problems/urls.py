from rest_framework import routers
from .views import ProblemViewSet, OptionViewSet


router = routers.DefaultRouter()
router.register('problems', ProblemViewSet, 'problems')
router.register('options', OptionViewSet, 'options')
urlpatterns = router.urls