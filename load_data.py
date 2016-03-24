import sys, os
#import urllib2
import csv
import django


# directory to outer parkpedia_project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# parkpedia_project/parkdata
PATH = os.path.join(BASE_DIR, 'parkdata')

# url path for csv
csv_parks = os.path.join(PATH, 'parks.csv')

# facilities csv
csv_facilities = os.path.join(PATH, 'facilities.csv')

# special features csv
csv_specialfeature = os.path.join(PATH, 'special_features.csv')

# do not need this line since we are accessing data locally; keep just in case we change
# response = urllib2.urlopen(csv_parks)  # using urllib2, grabs csv file from url


# park image csv file directory
csv_parkImages = os.path.join(PATH, 'park_images.csv')

your_djangoproject_home = BASE_DIR
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'parkpedia_project.settings'

from parkpedia.models import Park

dataPark = csv.reader(open(csv_parks))
dataFacilities = csv.reader(open(csv_facilities))
dataParkImages = csv.reader(open(csv_parkImages))
dataSpecialFeature = csv.reader(open(csv_specialfeature))

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

        for rows in dataParkImages:
            if rows[0] != 'park_id':
                if rows[0] == park.parkId:
                    park.imageURL = rows[1]
                    break

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
        # for row1 in dataSpecialFeature:
        #     if row1[0] != 'ParkID':
        #         if row1[0] == park.parkId:
        #             park.specialFeature = park.specialFeature + ' | ' + row1[1]
        #         else:
        #             park.save()
        #             break
