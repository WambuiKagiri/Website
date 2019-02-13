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

app_name = 'MySite'

admin.site.site_header = 'Desma Administration'
admin.site.site_title = 'Desma Administration'
admin.site.index_title ='Desma Administration'


urlpatterns = [
	url(r'^$', views.HomePageView.as_view(),name='index'),
	url(r'^chatindex/$', views.chatindex,name='chatindex'),
	# url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
	url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'login.html'}),
	url(r'^clientlogout/$', auth_views.LogoutView,{'template_name': 'clientlogout.html'}),
	url(r'^admin/', admin.site.urls),
	
	url(r'^about/$', views.AboutPageView.as_view(),name='about'),
	url(r'^contact/$', views.ContactPageView.as_view(),name='contact'),
	url(r'^ListProperty/$', views.ListPropertyPageView.as_view(),name='list_property'),
	url(r'^property/$', views.PropertyPageView.as_view(),name='property'),

	url(r'^properties/$', views.PropertiesPageView.as_view(),name='properties'),
	url(r'^requestedlistings/$', views.ListingsPageView.as_view()),
	url(r'^bookedviewings/$', views.BookingsPageView.as_view()),
	url(r'^agentt/messages/$', views.chats.as_view()),
	url(r'^property/(?P<property_title>[-\w]+)/(?P<pk>\d+)/$', views.PropertyPageView.as_view( )),
	
		
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

