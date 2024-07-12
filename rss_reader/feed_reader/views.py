import feedparser
from django.shortcuts import render
from django.core.cache import cache
from django.utils import timezone

def fetch_feed(url):
    cache_key = f'rss_feed_{url}'
    cache_time = 300  # Cache for 5 minutes
    # Try to get the feed from cache
    cached_feed = cache.get(cache_key)
    if cached_feed is not None:
        return cached_feed
    # If not in cache, fetch the feed
    try:
        feed = feedparser.parse(url)
        feed_data = {
            'feed_title': feed.feed.get('title', 'Unknown Feed'),
            'feed_entries': [],
            'last_updated': timezone.now(),
        }
        for entry in feed.entries[:5]:  # Display the first 5 entries
            feed_data['feed_entries'].append({
                'title': entry.get('title', 'No title'),
                'link': entry.get('link', '#'),
                'summary': entry.get('summary', 'No summary available'),
                'published': entry.get('published', 'No date available')
            })
        # Store in cache
        cache.set(cache_key, feed_data, cache_time)
        return feed_data
    except Exception as e:
        print(f"Error fetching feed {url}: {str(e)}")
        return None

def feed_list(request):
    feed_urls = [
        'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',
        'https://feeds.feedburner.com/ndtvnews-top-stories',
        'https://www.thehindu.com/news/feeder/default.rss',
        'https://www.hindustantimes.com/rss/topnews/rssfeed.xml',
        'https://indianexpress.com/feed/',
        'https://economictimes.indiatimes.com/rssfeedstopstories.cms',
        'https://zeenews.india.com/rss/india-national-news.xml',
    ]
    feeds = [feed for feed in (fetch_feed(url) for url in feed_urls) if feed is not None]
    context = {
        'feeds': feeds,
    }
    return render(request, 'feed_reader/feed_list.html', context)
