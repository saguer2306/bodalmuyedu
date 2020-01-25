from . import views
from django.urls import path


app_name = 'app_wed'

urlpatterns = [
	path('',views.guardar_invitado, name = 'confirmar'),
]