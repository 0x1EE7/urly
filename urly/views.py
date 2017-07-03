from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, RedirectView
from urly.forms import URLyForm
from urly.models import ShortUrl
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils import timezone


class UrlCreate(CreateView):
    '''
    Main view of urly app. Renders a form to enter target URL and
    redirects to URLSuccess to show generated URL
    '''
    template_name = 'urly/create.html'
    form_class = URLyForm

    def get(self, request):
        url_form = self.form_class()
        return render(request, self.template_name, {'form': url_form})

    def form_valid(self, form):
        # All url logic is done in ShortUrl.shorten_url()
        form.instance.url = ShortUrl.shorten_url(form.instance.target)
        form.instance.date = timezone.now()
        return super(UrlCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('created_url', kwargs={'url': self.object.url})


class UrlSuccess(TemplateView):
    template_name = 'urly/success.html'

    def get(self, request, *args, **kwargs):
        context = {'url': 'http://%s/%s' % (request.get_host(),
                                            self.kwargs['url'])}
        return self.render_to_response(context)


class UrlRedirect(RedirectView):
    '''
    This view redirects the short url in DB to absolute target URL
    '''

    def get_redirect_url(self, *args, **kwargs):
        self.url = get_object_or_404(ShortUrl, url=kwargs['url']).target
        return super(UrlRedirect, self).get_redirect_url(self, *args, **kwargs)
