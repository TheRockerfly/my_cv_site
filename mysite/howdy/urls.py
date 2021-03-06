from django.conf.urls import url
from howdy import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^cv/$', views.CvPageView.as_view()),
    url(r'^contact/$', views.ContactPageView.as_view())
]
