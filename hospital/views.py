from django.shortcuts import render
from django.http import JsonResponse
from .models import Hospital

def hospital_list(request):
    city = request.GET.get('city')
    district = request.GET.get('district')

    hospitals = Hospital.objects.all()
    if city:
        hospitals = hospitals.filter(city=city)
    if district:
        hospitals = hospitals.filter(district=district)

    cities = Hospital.objects.values_list('city', flat=True).distinct()

    return render(request, 'hospital/hospital_list.html', {
        'hospitals': hospitals,
        'cities': cities,
        'selected_city': city,
        'selected_district': district
    })


def get_districts(request):
    city = request.GET.get('city')
    districts = Hospital.objects.filter(city=city).values_list('district', flat=True).distinct()
    return JsonResponse(list(districts), safe=False)
