from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # regex
    # Examples:
    url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^sayHello','SayHello.views.sayHello'),
    
    url(r'^contacts','SayHello.views.contacts')
)
