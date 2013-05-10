from django.conf.urls import patterns, url


urlpatterns = patterns('favorite.views',
    url(r'^add-or-remove$', 'add_or_remove'),
)
