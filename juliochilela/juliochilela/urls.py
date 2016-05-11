from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin


urlpatterns = [
    # Examples:
     url(r'^$', 'juliochilela.views.en', name='en'),
     url(r'^pt/', 'juliochilela.views.pt', name='pt'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
