from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djdemo.views.home', name='home'),
    # url(r'^djdemo/', include('djdemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^hello[/]?$', 'djdemo.views.hello', name='hello'),

    url(r'^time[/]?$', 'djdemo.views.time', name='time'),

    # 404 view
    url(r'^.*$', 'djdemo.views.notfound', name='notfound'),
)
