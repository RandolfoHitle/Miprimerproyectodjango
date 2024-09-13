from django.urls import path
from .views import (
    PaisListView, PaisCreateView, PaisUpdateView, PaisDeleteView,
    DepartamentoListView, DepartamentoCreateView, DepartamentoUpdateView, DepartamentoDeleteView,
    MunicipioListView, MunicipioCreateView, MunicipioUpdateView, MunicipioDeleteView,
    PaisViewSet, DepartamentoViewSet, MunicipioViewSet
)
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('paises/', PaisListView.as_view(), name='pais_list'),
    path('paises/create/', PaisCreateView.as_view(), name='pais_create'),
    path('paises/<int:pk>/update/', PaisUpdateView.as_view(), name='pais_update'),
    path('paises/<int:pk>/delete/', PaisDeleteView.as_view(), name='pais_delete'),
    
    path('departamentos/', DepartamentoListView.as_view(), name='departamento_list'),
    path('departamentos/create/', DepartamentoCreateView.as_view(), name='departamento_create'),
    path('departamentos/<int:pk>/update/', DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('departamentos/<int:pk>/delete/', DepartamentoDeleteView.as_view(), name='departamento_delete'),
    
    path('municipios/', MunicipioListView.as_view(), name='municipio_list'),
    path('municipios/create/', MunicipioCreateView.as_view(), name='municipio_create'),
    path('municipios/<int:pk>/update/', MunicipioUpdateView.as_view(), name='municipio_update'),
    path('municipios/<int:pk>/delete/', MunicipioDeleteView.as_view(), name='municipio_delete'),
]

# Rutas API
router = DefaultRouter()
router.register(r'paises', PaisViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'municipios', MunicipioViewSet)

urlpatterns += router.urls
