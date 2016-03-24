import sys, os
import urllib2
import csv
import django

# directory to outer parkpedia_project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# url path for csv
csv_parks = os.path.join(BASE_DIR, 'test.csv')


# facilities csv file directory
csv_facilities = os.path.join(BASE_DIR, 'test_facilities.csv')


your_djangoproject_home = BASE_DIR
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'parkpedia_project.settings'

from parkpedia.models import Park

dataPark = csv.reader(open(csv_parks))
dataFacilities = csv.reader(open(csv_facilities))

django.setup()

# flushes out the database
p = Park.objects.all()
p.delete()

for row in dataPark:
    if row[0] != 'ParkID':  # Ignore the header row, import everything else
        park = Park()
        park.parkId = row[0]
        park.name = row[1]
        park.streetNum = row[3]
        park.streetName = row[4]
        park.latLon = row[7]

        if row[14] == "N":
            park.washroom = "No"

        if row[14] == "Y":
            park.washroom = "Yes"

        for row0 in dataFacilities:
                if row0[0] != 'ParkID':
                    if row0[0] == park.parkId:
                        if park.facilities == "None":
                            park.facilities = ""
                        park.facilities = park.facilities + ' | ' + row0[2]

                    else:
                        park.save()
                        break
        park.save()