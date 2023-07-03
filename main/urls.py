from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import home_view, category_view, region_view, news_detail_view, tags_view, chosen_view, ads_view, \
    videonews_view, articles_view, interviews_view, breaking_news_view, inquiries_view, photonews_view

urlpatterns = [
    path('', home_view, name='home'),
    path('category/<int:pk>', category_view, name='category'),
    path('region/<int:pk>', region_view, name='region'),
    path('news/<int:pk>', news_detail_view, name='news_detail'),
    path('news/tag/<int:pk>', tags_view, name='tags'),

    path('chosen', chosen_view, name='chosen'),
    path('ads', ads_view, name='ads'),
    path('videonews', videonews_view, name='videonews'),
    path('articles', articles_view, name='articles'),
    path('interviews', interviews_view, name='interviews'),
    path('breaking_news', breaking_news_view, name='breaking_news'),
    path('inquiries', inquiries_view, name='inquiries'),
    path('photonews', photonews_view, name='photonews'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
