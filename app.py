import folium
import pandas
file=pandas.read_csv("Volcanoes.txt")


lat=list(file.LAT)
lon=list(file.LON)
ele=list(file.ELEV)

def color_selector(eleva):
    if(eleva<1000):
        return("green")
    elif(3000>eleva>1000):
         return("blue")
    elif(eleva>3000):
         return("red")
#for i in range(0,len(lat)-1):
          #print(str(a[i])+ " ," + str(b[i]) )
#          fg.add_child(folium.Marker(location=[lat[i],lon[i]], popup="Volcanoes",icon=folium.Icon(color="red")))
map=folium.Map(location=[22,77.4],zoom_start=3,tiles="Mapbox Bright")

fg1=folium.FeatureGroup(name="my cities")
for i in [[13,80],[21.9,77.7],[23.2,77.4]]:
      fg1.add_child(folium.Marker(location=i,popup="my cities",icon=folium.Icon("color=green")))




fg =folium.FeatureGroup(name="Volacnoes")


for i, j, el in zip(lat,lon,ele):
                 fg.add_child(folium.CircleMarker(location=[i,j],radius=4,fill_opacity=.8, popup=str(el)+ " " +"m",color="grey",fill_color=color_selector(el)))


fg2 =folium.FeatureGroup(name="Population")

fg2.add_child(folium.GeoJson(data=open('world.json','r', encoding="utf-8-sig"),
style_function=lambda x:{'fillColor':"green" if x['properties']['POP2005']< 10000000
else 'orange' if 10000000<= x['properties']['POP2005']< 20000000 else 'red'}))



map.add_child(folium.features.ClickForMarker(popup=None))
map.add_child(fg)
map.add_child(fg2)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save("map1.html")
