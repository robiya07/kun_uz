from main.models import CategoryModel, ZoneModel, NewsModel


def header_view(request):
    main_categories = CategoryModel.objects.all()
    zones = ZoneModel.objects.all()
    context = {
        'main_categories': main_categories,
        'zones': zones
    }
    return context


def last_news(request):
    news = NewsModel.objects.all()[:7]
    return {'news': news}


# def recommended_view(request):
#     more_views = NewsModel.objects.order_by('-hit_count_generic__hits')[:4]
#     recommended = NewsModel.objects.order_by('-hit_count_generic__hits')[4:8]
#     return {'recommended': recommended, 'more_views': more_views}
