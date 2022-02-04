from django.urls import path
from .import views 
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.projects,name="projects"),
    path('project/<str:pk>/', views.project,name="project"),
    path('create-form', views.createForm,name="create-form"),
    path('updateProject/<str:pk>/', views.updateProject,name="updateProject"),
    path('deleteProject/<str:pk>/', views.deleteProject,name="deleteProject"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
