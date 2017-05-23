from django.conf.urls import *
from students import views as myapp_views
from django.contrib import admin

urlpatterns = [
    #Students Url's
        url(r'^$', myapp_views.students_list, name = 'home'),
        url(r'^students/add/$', myapp_views.students_add, name='students_add'),
        url(r'^students/(?P<sid>\d+)/edit/$', myapp_views.students_edit, name='students_edit'),
        url(r'^students/(?P<sid>\d+)/delete/$', myapp_views.students_delete, name='students_delete'),
    #Froups Url'
        url(r'^groups/$', myapp_views.groups_list, name='groups'),
        url(r'^groups/add/$', myapp_views.groups_add, name='groups_add'),
        url(r'^groups/(?P<gid>\d+)/edit/$', myapp_views.groups_edit, name='groups_edit'),
        url(r'^groups/(?P<gid>\d+)/delete/$', myapp_views.groups_delete, name='groups_delete'),

    #Admin
        url(r'^admin/', include(admin.site.urls)),
                ]
