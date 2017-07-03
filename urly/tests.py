from django.test import TestCase
from urly.models import ShortUrl
from django.utils import timezone


class ShortUrlTest(TestCase):
    def setUp(self):
        self.tc_url = 'http://techcrunch.com/2012/12/28/pinterest-lawsuit/'
        self.matching_url = 'lawsuit'
        self.non_matching_url = 'qweaszxc'
        ShortUrl.objects.create(url=self.matching_url)
        ShortUrl.objects.create(url=self.non_matching_url)

    def test_shorten_url_basic(self):
        short_url = ShortUrl.shorten_url(self.tc_url)
        self.assertEqual(short_url, self.matching_url,
                         "Expected: '%s' but returned: '%s' "
                         % (self.matching_url, short_url))
        s_url = ShortUrl.objects.get(url=short_url)
        s_url.target = self.tc_url
        s_url.date = timezone.now()
        s_url.save()

        same_short_url = ShortUrl.shorten_url(self.tc_url)

        self.assertEqual(same_short_url, short_url,
                         "Valid target in db should return immediately")

    def test_shorten_url_non_matching(self):
        s = ShortUrl.objects.get(url=self.matching_url)
        s.target = 'http://www.fyndiq.se/'
        s.save()
        short_url = ShortUrl.shorten_url(self.tc_url)
        self.assertEqual(short_url, self.non_matching_url,
                         "Expected: '%s' but returned: '%s' "
                         % (self.non_matching_url, short_url))

    def test_shorten_url_delete_old(self):
        urls = ShortUrl.objects.all()
        first = urls[0]
        for s_url in urls:
            s_url.target = self.tc_url
            s_url.date = timezone.now()
            s_url.save()
        short_url = ShortUrl.shorten_url(self.tc_url)
        self.assertEqual(short_url, first.url,
                         "Should return oldest url:'%s' but returned: '%s'"
                         % (first.url, short_url))
