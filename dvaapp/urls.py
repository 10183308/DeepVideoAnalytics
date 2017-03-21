from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^$', views.index, name='app'),
    url(r'^status$', views.status, name='status'),
    url(r'^indexes', views.indexes, name='indexes'),
    url(r'^external', views.external, name='external'),
    url(r'^youtube$', views.yt, name='youtube'),
    url(r'^videos/$', views.VideoList.as_view()),
    url(r'^queries/$', views.QueryList.as_view()),
    url(r'^Search$', views.search),
    url(r'^videos/(?P<pk>\d+)/$', views.VideoDetail.as_view(), name='video_detail'),
    url(r'^frames/$', views.FrameList.as_view()),
    url(r'^frames/(?P<pk>\d+)/$', views.FrameDetail.as_view(), name='frames_detail'),
    url(r'^queries/(?P<pk>\d+)/$', views.QueryDetail.as_view(), name='query_detail'),
    url(r'^retry/(?P<pk>\d+)/$', views.retry_task, name='restart_task'),
    url(r'^requery/(?P<query_pk>\d+)/$', views.index, name='requery'),
    url(r'^query_frame/(?P<frame_pk>\d+)/$', views.index, name='query_frame'),
    url(r'^query_detection/(?P<detection_pk>\d+)/$', views.index, name='query_detection'),
    url(r'^annotate_frame/(?P<frame_pk>\d+)/$', views.annotate, name='annotate_frame'),
    url(r'^annotate_detection/(?P<detection_pk>\d+)/$', views.annotate, name='annotate_detection'),
    url(r'^delete', views.delete_object, name='delete_object')
]
