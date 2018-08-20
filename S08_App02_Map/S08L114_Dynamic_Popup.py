import folium
import pandas

data = pandas.read_csv("data/Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln],
                               popup=str(el)+" m",
                               icon=folium.Icon(color='darkpurple')))
map.add_child(fg)

map.save("data/Map1.html")

# you may get a blank webpage if there are quotes(') in the strings.
# To avoid that change the popup argument to:
# popup=folium.Popup(str(el), parse_html=True))
