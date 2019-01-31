from django.conf.urls import url, include
from MySite import views
from django.contrib import admin
from .views import SuccessPageView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'MySite'

admin.site.site_header = 'Desma Administration'
admin.site.site_title = 'Desma Administration'
admin.site.index_title ='Desma Administration'


urlpatterns = [
	url(r'^$', views.HomePageView.as_view(),name='index'),
	url(r'^admin/', admin.site.urls),
	url(r'^about/$', views.AboutPageView.as_view(),name='about'),
	url(r'^contact/$', views.ContactPageView.as_view(),name='contact'),
	url(r'^ListProperty/$', views.ListPropertyPageView.as_view(),name='list_property'),
	url(r'^property/$', views.PropertyPageView.as_view(),name='property'),
	url(r'^search/$', views.SearchPageView.as_view(),name='search'),
	url(r'^properties/$', views.PropertiesPageView.as_view(),name='properties'),
	url(r'^success/$', views.SuccessPageView.as_view(),name='success'),
	url(r'^agent/$', views.AgentPageView.as_view(),name='agent'),
	url(r'^agentlogin/$', views.AgentLogInPageView.as_view(),name='agentlogin'),
	url(r'^property/(?P<property_title>[-\w]+)/BookViewing/$', views.BookViewingPageView.as_view()),
	url(r'^property/(?P<property_title>[-\w]+)/$', views.PropertyPageView.as_view( )),
	url(r'^Latest/(?P<property_title>[-\w]+)/$', views.LatestPageView.as_view(),name='latest'),
	
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

