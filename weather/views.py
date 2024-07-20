from django.shortcuts import render
from django.utils import timezone
from .forms import CityForm
from .utils import get_weather
from django.http import JsonResponse
from .models import CitySearch
from django.db.models import Count
def index(request):
    user = request.user if request.user.is_authenticated else None
    weather_data = None
    searches = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather(city)
            if weather_data:
                if user:
                    search, created = CitySearch.objects.get_or_create(user=user, city_name=city)
                    if not created:
                        search.search_count += 1
                        search.last_searched = timezone.now()
                        search.save()
    else:
        form = CityForm()
        if user:
            searches = CitySearch.objects.filter(user=user).order_by('-last_searched')[:5]

    return render(request, 'weather/index.html', {'form': form, 'weather_data': weather_data, 'searches': searches})






def search_statistics(request):
    statistics = CitySearch.objects.values('city_name').annotate(search_count=Count('city_name'))
    data = list(statistics)
    return JsonResponse(data, safe=False)

def autocomplete(request):
    if 'term' in request.GET:
        term = request.GET['term']
        # Поиск городов, содержащих 'term', и сортировка по количеству запросов
        cities = CitySearch.objects.filter(city_name__icontains=term).order_by('-search_count').distinct()
        results = [{'label': city.city_name, 'value': city.city_name} for city in cities]
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)
