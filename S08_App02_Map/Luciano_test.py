import folium

map = folium.Map(location=[-23.559, -46.678], zoom_start=10, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[-23.559, -46.678],
                           popup="Aqui habita uma bixona louca",
                           icon=folium.Icon(color='lightred')))
map.add_child(fg)

map.save("data/Map_Jeb.html")
