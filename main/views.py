from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from hitcount.templatetags.hitcount_tags import get_hit_count
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

from main.models import CategoryModel, NewsModel, ZoneModel, TagModel


# Create your views here.

def home_view(request):
    last_posts = NewsModel.objects.all()[:5]
    chosen = NewsModel.objects.filter(is_chosen=True)[:3]
    breaking_news = NewsModel.objects.filter(is_breaking_new=True)[:5]
    interviews = NewsModel.objects.filter(is_interview=True)[:4]
    inquiries = NewsModel.objects.filter(is_inquiry=True)[:5]
    articles = NewsModel.objects.filter(is_article=True)[:6]
    ads = NewsModel.objects.filter(is_ad=True)[:4]
    video_news = NewsModel.objects.filter(is_video_news=True)[:3]
    photo_news = NewsModel.objects.filter(is_photo_news=True)[:3]

    q = request.GET.get('q')
    if q:
        search_posts = NewsModel.objects.filter(Q(title__icontains=q) | Q(short_description__icontains=q))
        context = {
            'search_posts': search_posts,
            'q': q
        }
        return render(request, 'main/tags.html', context)
    else:
        q = ''

    context = {
        'last_posts': last_posts,
        'chosen': chosen,
        'interviews': interviews,
        'breaking_news': breaking_news,
        'inquiries': inquiries,
        'articles': articles,
        'ads': ads,
        'video_news': video_news,
        'photo_news': photo_news,
        'q': q
    }
    return render(request, 'main/home.html', context)


def chosen_view(request):
    chosen_list = NewsModel.objects.filter(is_chosen=True)
    return render(request, 'main/home_categories.html', {'l': chosen_list})


def breaking_news_view(request):
    breaking_news_list = NewsModel.objects.filter(is_breaking_new=True)
    return render(request, 'main/home_categories.html', {'l': breaking_news_list})


def interviews_view(request):
    interviews_list = NewsModel.objects.filter(is_interview=True)
    return render(request, 'main/home_categories.html', {'l': interviews_list})


def inquiries_view(request):
    inquiries_list = NewsModel.objects.filter(is_inquiry=True)
    return render(request, 'main/home_categories.html', {'l': inquiries_list})


def articles_view(request):
    articles_list = NewsModel.objects.filter(is_article=True)
    return render(request, 'main/home_categories.html', {'l': articles_list})


def ads_view(request):
    ads_list = NewsModel.objects.filter(is_ad=True)
    return render(request, 'main/home_categories.html', {'l': ads_list})


def videonews_view(request):
    vslugeo_news_list = NewsModel.objects.filter(is_vslugeo_news=True)
    return render(request, 'main/home_categories.html', {'l': vslugeo_news_list})


def photonews_view(request):
    photo_news_list = NewsModel.objects.filter(is_photo_news=True)
    return render(request, 'main/home_categories.html', {'l': photo_news_list})


def region_view(request, slug):
    posts = NewsModel.objects.filter(zone__slug=slug)
    region = ZoneModel.objects.get(slug=slug)
    return render(request, 'main/region.html', {'posts': posts, 'region': region})


def category_view(request, slug):
    posts_c = NewsModel.objects.filter(category__slug=slug)
    category = CategoryModel.objects.get(slug=slug)
    return render(request, 'main/category.html', {'posts_c': posts_c, "category": category})


def news_detail_view(request, slug):
    news_det = NewsModel.objects.get(slug=slug)
    ads = NewsModel.objects.filter(is_ad=True)[:4]
    hit_count = get_hitcount_model().objects.get_for_object(news_det)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    return render(request, 'main/news_detail.html', {'post_detail': news_det, 'ads': ads, 'hit_count_obj': hit_count_response})


def tags_view(request, slug, page):
    tag = TagModel.objects.get(slug=slug)
    news_t = tag.news.all()

    paginator = Paginator(news_t, 18)

    try:
        news_t = paginator.page(page)
    except EmptyPage:
        news_t = paginator.page(paginator.num_pages)

    return render(request, 'main/tags.html', {'news_t': news_t, 'tag': tag})


def last_posts(request, page):
    last = NewsModel.objects.all()
    paginator = Paginator(last, 15)

    try:
        last = paginator.page(page)
    except EmptyPage:
        last = paginator.page(paginator.num_pages)

    return render(request, 'main/last_posts.html', {'last': last})


def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)