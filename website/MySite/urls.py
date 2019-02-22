from django.conf.urls import url, include
from MySite import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from MySite import views as mysite_views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from MySite.consumers import ChatConsumer, TaskConsumer
from MySite.views import dashboard,home,subscribe,search,listproperty,message
from MySite.views import agentprofile
from django.views.generic import TemplateView
app_name = 'MySite'

admin.site.site_header = 'Desma Administration'
admin.site.site_title = 'Desma Administration'
admin.site.index_title ='Desma Administration'


urlpatterns = [
	url(r'^$', home ,name='index'),
	url(r'^chatindex/$', views.chatindex,name='chatindex'),
	# url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
	url(r'^admin/', admin.site.urls),
	url(r'^about/$', views.AboutPageView.as_view(),name='about'),
	url(r'^contact/$', views.ContactPageView.as_view(),name='contact'),
	url(r'^ListProperty/$', listproperty ,name='list_property'),
	url(r'^property/$', views.PropertyPageView.as_view(),name='property'),
	url(r'^properties/$', views.PropertiesPageView.as_view(),name='properties'),
	url(r'^requestedlistings/$', views.ListingsPageView.as_view()),
	url(r'^bookedviewings/$', views.BookingsPageView.as_view()),
	url(r'^message/$', message,name='chat'),
	url(r'^property/(?P<property_title>[-\w]+)/(?P<pk>\d+)/$', views.PropertyPageView.as_view( )),
	url(r'^agent/profile/$', agentprofile),
	# url(r'^/message/', TemplateView.as_view(template_name='message.html'))

		
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

