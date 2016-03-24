from parkpedia.models import Park, FavouritePark
from parkpedia.forms import FavouriteParkForm
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import json


def index(request):
    search = 0
    lat = 0
    lon = 0
    errors = []
    favparks = []
    try:
        if request.user.is_authenticated():
            username = request.user.username
            favparks = FavouritePark.objects.filter(username=username)

    except ObjectDoesNotExist:
        errors.append('No favourite parks saved')

    allParks = Park.objects.all()
    allParkNames = []
    for park in allParks:
        allParkNames.append(park.name)

    json_list = json.dumps(allParkNames)

    if 'q' in request.GET:
        # q = user's input is not valid
        q = request.GET['q']

        # nothing is entered in the search box
        if not q:
            errors.append('Please enter a park to search')

        else:
            try:
                park = Park.objects.get(name__iexact=q)

                #get the park image URL(example http://cfapp.vancouver.ca/parks/parks/images/adanac_title.jpg)
                parkImageUrl = park.imageURL
                fullImageUrl = 'http://cfapp.vancouver.ca'+parkImageUrl

                # convert lat lon string into lat lon numbesr
                parkLat = park.latLon
                latlon = parkLat.replace(' ', '').split(',')
                lat = latlon[0]
                lat = float(lat)
                lon = latlon[1]
                lon = float(lon)

                # park special features


                # create a park facilities array
                parkFacilities = park.facilities
                parkFacilitiesArray = parkFacilities.split('|')
                # json_list_facilities = json.dumps(ParkFacilitiesArray)


                search = 1

                return render(request, 'parkpedia/index.html',
                              {'park': park, 'query': q, 'lat': lat, 'lon': lon, 'search': search,
                               'allParkNames': allParkNames, 'json_list': json_list,
                               'parkFacilitiesArray': parkFacilitiesArray, 'favparks' : favparks,
                               'fullImageUrl': fullImageUrl, })

            # if park entered is not a park in the database
            except ObjectDoesNotExist:
                errors.append('Sorry, that is not a park')

    return render(request, 'parkpedia/index.html',
                  {'errors': errors, 'search': search, 'lat': lat, 'lon': lon, 'allParkNames': allParkNames,
                   'json_list': json_list, 'favparks' : favparks,})


@login_required(login_url='/')
def favourite_park(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = FavouriteParkForm(request.POST)

        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.username = request.user.username
            stock.save()
            return redirect('/')

        else:
            print form.errors

    else:
        form = FavouriteParkForm()

    context_dict = {'form': form}

    return render_to_response('parkpedia/fav.html', context_dict, context)


def logout(request):
    auth_logout(request)
    return redirect('/')
