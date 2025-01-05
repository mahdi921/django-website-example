from django.urls import path
from django.contrib.sitemaps.views import sitemap
from testing.sitemaps import StaticViewSitemap
from testing.views import index_view, about_view, contact_view, form_test_view, newsletter_view
from blog.sitemaps import BlogSitemap

app_name = 'testing'

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('form-test', form_test_view, name='form-test'),
    path('newsletter', newsletter_view, name='newsletter'),
path(
    "sitemap.xml",
    sitemap,
    {"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap",
),
    ]