

from accounts import views
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.contrib import admin


urlpatterns = [

    path('admin/', admin.site.urls),
    path('get_videos/', views.get_video_names, name='get_video_names'),
    path('get_transcript/<int:video_id>/', views.get_transcript, name='get_transcript'),
    path('get_names/', views.get_summary_names, name='get_summary_names'),
    path('get_summary/<int:summary_id>/', views.get_summary, name='get_summary'),
     path('get_analysis_names/', views.get_analysis_names, name='get_analysis_names'),
    path('get_analysis/<int:analysis_id>/', views.get_analysis, name='get_analysis'),
    path('get_report_names/', views.get_report_names, name='get_report_names'),
     path('get_report/<str:report_name>/', views.get_report, name='get_report'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]


urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]