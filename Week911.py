import math
import urllib.request

location1 = input("Enter a location: ")
location2 = input("Enter a second location: ")
loc1= location1.replace(" ", "%20")
loc2= location2.replace(" ", "%20")
#response = str(urllib.request.urlopen("https://nominatim.openstreetmap.org/search?q=" + "query" + "&format=xml").read(),'utf-8')
base_url = "https://nominatim.openstreetmap.org/search?q=<query>&format=xml&accept-language=en"

url1 = base_url.replace("<query>", loc1)
url2 = base_url.replace("<query>", loc2)

#print(url1)
#print(url2)

response1 = str(urllib.request.urlopen(url1).read(),'utf-8')
response2 = str(urllib.request.urlopen(url2).read(),'utf-8')

lat_pos = response1.find("lat=")
lat_pos1 = response1.find("'", lat_pos)
lat_pos2 = response1.find("'", lat_pos1 +1)
lat1 = float(response1[lat_pos1+1:lat_pos2])


lon_pos = response1.find("lon=")
lon_pos1 = response1.find("'", lon_pos)
lon_pos2 = response1.find("'", lon_pos1 +1)
lon1 = float(response1[lon_pos1+1:lon_pos2])


lat_pos2 = response2.find("lat=")
lat_pos1_2 = response2.find("'", lat_pos2)
lat_pos2_2 = response2.find("'", lat_pos1_2 +1)
lat2 = float(response2[lat_pos1_2+1:lat_pos2_2])


lon_pos2 = response2.find("lon=")
lon_pos1_2 = response2.find("'", lon_pos2)
lon_pos2_2 = response2.find("'", lon_pos1_2 +1)
lon2 = float(response2[lon_pos1_2+1:lon_pos2_2])


name = response1.find("display_name=")
name1 = response1.find("'", name)
name2 = response1.find("'", name1 + 1)
Dname = str(response1[name1+1:name2])
y = Dname.split(", ")
if len(y) < 3:
	y=y
else:
	y1 = ', '.join(y[0:3])
	

name2 = response2.find("display_name=")
name1_2 = response2.find("'", name2)
name2_2 = response2.find("'", name1_2 +1)
Dname2 = str(response2[name1_2+1:name2_2])
x = Dname2.split(", ")
if len(x) < 3:
	x=x
else:
	x1 = ', '.join(x[0:3])
def ToRadians (deg):
	deg = deg *(math.pi/180)
	return deg
sin = math.sin
cos = math.cos
arcsin = math.asin
def Distance (lat1, lat2, lon1, lon2):
	a = sin((ToRadians(lat2)-ToRadians(lat1))/2)**2 + cos(ToRadians(lat1)) * cos(ToRadians(lat2)) * sin((ToRadians(lon2)-ToRadians(lon1))/2)**2
	b = 2*arcsin(math.sqrt(a))
	dist = 3959 * b
	return dist
z = Distance(lat1, lat2, lon1, lon2)
print(y1 + " " + "is" + " " + "{0:0.1f}".format(z) + " " + "miles" + " " + "away" + " " +"from" + " " + x1 + ".")