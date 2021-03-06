from django.conf.urls import url
from django.contrib.auth.views import logout
from main import views, bot_views

app_name = 'main'

urlpatterns = [
    url(r'^$',views.nill,name='nill'),

	#Login, SignUp urls
	url(r'^register/?',views.register,name='register'),
	url(r'^email_confirm/(?P<token>\w+)/?',views.email_confirm,name = 'email_confirm'),
	url(r'^login/?',views.login_view,name='login'),

	#url which returns JSON of is_safe and paramters
	url(r'^get_location/?',views.get_location,name='get_location'),

	url(r'^upload_csv/?', views.upload_csv, name='upload_csv'),

	url(r'^get_food_location/?',views.get_food_location,name='get_food_location'),

	#url to update device token on refresh from the app
	url(r'^update_device_token/?',views.update_device_token,name='update_device_token'),

	#url to send push notifications and sms
	url(r'^auto_notify/?',views.auto_notify,name='auto_notify'),

	#urls to update location and safe status
	url(r'^update_location/?',views.update_location,name='update_location'),
	url(r'^send_sms/?',views.send_sms,name='send_sms'),
	url(r'^update_safe_status/?',views.update_safe_status,name='update-safe_status'),

	#chat bot urls
	url(r'^command_response/?',bot_views.command_response,name='command_response'),

]