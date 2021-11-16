from django.urls import path


from . import views

urlpatterns = [
    path('taxa/<str:scientific_name>/', views.get_taxon),
    path('taxa/', views.get_taxa),
    path('synonyms/<str:scientific_name>/', views.get_taxon_synonyms),
    path('synonyms/', views.get_synonyms),
]
