from django.conf.urls import url

from . import views

app_name = 'imageModifier'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<campaign_pk>\d+)/select-logos/$', views.select_upload_campaign_logos, name='select_upload_campaign_logos'),
    url(r'^upload_company_image/$', views.upload_company_image, name='uploadCompanyImage'),
    url(r'^(?P<user_proposition_pk>\d+)/upload-picture/$', views.upload_transformable_image, name='uploadTransformableImage'),
    url(r'^current-campaigns/$', views.user_propositions_list, name='user_propositions_list'),
    url(r'^(?P<user_proposition_pk>\d+)/$', views.user_proposition_detail, name='user_proposition_detail'),
    url(r'^image-processing/(?P<user_proposition_pk>\d+)/$', views.image_processing, name='image_processing'),
    url(r'^select-campaign/$', views.worker_select_campaign, name='worker_select_campaign'),
]
