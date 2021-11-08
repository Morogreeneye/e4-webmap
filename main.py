import folium
import csv

MAPNAME = "data/map1.html"

if __name__ == "__main__":
    print("Hello gang.")
    map = folium.Map(location=(35.61, -82.44))
    map.save('map1.html')

    with open("volcano-events.txt") as csvfile:
        sniffsnaff = csv.Sniffer().sniff(csvfile.read())
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=sniffsnaff)
        rows = []
        for row in reader:
            rows.append(row)
