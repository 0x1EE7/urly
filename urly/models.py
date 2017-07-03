from django.db import models
from urlparse import urlparse
import re


class ShortUrl(models.Model):
    url = models.CharField(max_length=200, primary_key=True)
    target = models.URLField(blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '%s -> %s' % (self.url, self.target)

    @staticmethod
    def shorten_url(target):
        '''
        Tokenizes the target url an returns a matching keyword from database
        accordingly.If no keyword is matched a random available key is
        returned. If all keys are in use the oldest key is returned.
        '''
        # Clean and tokenize url. host is eliminated with urlparse().path
        url_candidates = re.split(r'[^a-zA-Z]*', urlparse(target).path)
        short_url_query = ShortUrl.objects.filter(pk__in=url_candidates)
        if short_url_query.count() > 0:
            # At least one token is part of wordlist
            for short_url in short_url_query:
                # If given target already has short url return immedeately
                if (short_url.target == target) or len(short_url.target) == 0:
                    return short_url.url

        # No token is in our database. Get a random short url
        try:
            url = ShortUrl.objects.filter(target__exact=''
                                          ).order_by('?')[:1].get().url
        except ShortUrl.DoesNotExist:
            # All keywords must be used.
            # Delete oldest short_url object
            short_url_to_remove = ShortUrl.objects.earliest('date')
            url = short_url_to_remove.url
            short_url_to_remove.delete()
        return url
