from .views import StudentViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('student', StudentViewSet)
urlpatterns = router.urls