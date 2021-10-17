Für die Erstellung der geojson Daten sind folgende Schritte notwendig:
1. Umwandeln der Excel Tabelle in eine .csv Datei
2. Programm starten
3. csv-Datei öffnen
4. Eventuell Zusatzdaten auswählen (z.B. Stadtteilgrenzen)
5. Speicherort auswählen 
6. Fertig.

Die generierte Datei kann dann einfach mittels des Leaflet Plugins in eine Webseite eingebunden werden.
Zum Beipiel:

[leaflet-map zoom=9  height=800  scrollwheel]

[leaflet-geojson circleMarker radius=6 color='#46962b' weight=4 fill=on fillOpacity=0.5 src=https://raw.githubusercontent.com/SaschaKaden/maps/main/Infostaende.geojson fitbounds=1]{popup-text}[/leaflet-geojson]

