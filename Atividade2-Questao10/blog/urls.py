from django.urls import re_path
from blog import views



urlpatterns = [
    re_path(
        r'^blog/$',
        views.lista_posts,
        name='lista_posts'
    ),

    re_path(
        r'^blog/post/(?P<ano>20(0[0-9]|1[0-9]|2[0-9]|30))/(?P<mes>0[1-9]|1[0-2])/(?P<slug>[-\w]+)/$',
        views.post,
        name='post_detalhe'
    ),
]