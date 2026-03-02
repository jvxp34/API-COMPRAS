from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ProductViewSet, ListaCompraViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'produtos', ProductViewSet)
router.register(r'listas', ListaCompraViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = router.urls