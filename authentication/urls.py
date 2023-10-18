

from accounts import views
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [

    path('get_videos/', views.get_video_names, name='get_video_names'),
    path('get_transcript/<int:video_id>/', views.get_transcript, name='get_transcript'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]


urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]