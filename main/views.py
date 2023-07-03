from django.shortcuts import render

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

    context = {
        'last_posts': last_posts,
        'chosen': chosen,
        'interviews': interviews,
        'breaking_news': breaking_news,
        'inquiries': inquiries,
        'articles': articles,
        'ads': ads,
        'video_news': video_news,
        'photo_news': photo_news
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
    video_news_list = NewsModel.objects.filter(is_video_news=True)
    return render(request, 'main/home_categories.html', {'l': video_news_list})


def photonews_view(request):
    photo_news_list = NewsModel.objects.filter(is_photo_news=True)
    return render(request, 'main/home_categories.html', {'l': photo_news_list})


def region_view(request, pk):
    posts = NewsModel.objects.filter(zone__id=pk)
    region = ZoneModel.objects.get(id=pk)
    return render(request, 'main/region.html', {'posts': posts, 'region': region})


def category_view(request, pk):
    posts_c = NewsModel.objects.filter(category__id=pk)
    category = CategoryModel.objects.get(id=pk)
    return render(request, 'main/category.html', {'posts_c': posts_c, "category": category})


def news_detail_view(request, pk):
    news_det = NewsModel.objects.get(id=pk)
    ads = NewsModel.objects.filter(is_ad=True)[:4]
    return render(request, 'main/news_detail.html', {'post_detail': news_det, 'ads': ads})


def tags_view(request, pk):
    tag = TagModel.objects.get(id=pk)
    news_t = tag.news.all()
    return render(request, 'main/tags.html', {'news_t': news_t, 'tag': tag})
