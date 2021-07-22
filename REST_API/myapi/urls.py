from django.urls import path
from .views import *

urlpatterns = [
	path('cars/post/', CarCreateAPI.as_view()),
	path('cars/get/', CarAPI.as_view()),
	path('cars/put/<int:pk>/', CarUpdateAPI.as_view()),
	path('cars/delete/<int:pk>/', CarDeleteAPI.as_view()),
	path('dealers/post/', DealerCreateAPI.as_view()),
	path('dealers/get/', DealerAPI.as_view()),
	path('dealers/put/<int:pk>/', DealerUpdateAPI.as_view()),
	path('dealers/delete/<int:pk>/', DealerDeleteAPI.as_view())
] 