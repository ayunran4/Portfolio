from django.conf.urls import url

urlpatterns = [
    url(r'^$', include('certificate.urls')),    # $는 빈 경로
]
