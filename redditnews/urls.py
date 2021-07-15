from django.conf.urls import include, url
from . import views
from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns=[
    url(r'^$',views.index, name='index'),
    url('register/',views.register, name='register'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    # url(r'profile/', views.profile, name='profile'),
    url(r'^create/', views.create, name="create"),
    url(r'^profile/(?P<fk>[0-9]+)', views.profileview, name="profile"),
]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)