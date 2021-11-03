import folium
MAPNAME = "data/map1.html"

if __name__=="__main__":
    print("Hello gang.")
    map = folium.Map(location=(35.61, -82.44))
    map.save('map1.html')