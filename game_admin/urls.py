from django.conf.urls   import url
from django.conf.urls   import include
from django.contrib     import admin

from base               import views


urlpatterns = [

    url(r'^$', views._login),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^players_list/$', views.search_form),
    url(r'^players/$', views.search),
    url(r'^players_change_xp/([0-9]+)/$', views.players_change_xp),
    url(r'^changed_xp/([0-9]+)/$', views.changed_xp),
    url(r'^logout/$', views._logout),
    url(r'^login/$', views._login),
    url(r'^home/$', views.home),
    url(r'^invaild_input/$', views.invalid_input),
    url(r'^stat_players/$', views.stat_players),
    url(r'^stat_players/result$', views.stat_players_result),

]
