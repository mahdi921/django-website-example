from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post
from django.utils import timezone


class LatestEntriesFeed(Feed):
    title = "Newest posts from our blog"
    link = "/rss/feed"
    description = "Updates on blog that our users have posted."

    @staticmethod
    def items():
        return Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100] + '...'