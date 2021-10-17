import csv
import json
from src.feature import Feature
import easygui


def load_csv():
    file_type = ('*.csv')
    path = easygui.fileopenbox(default=file_type, title='Laden der Tabelle mit den Features', filetypes=file_type)
    if path is None or not path.lower().endswith(('.csv', '.xlsx')):
        print('wrong file type')
        return []

    with open(path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')

        line_count = 0
        count = 0
        features = []
        id_index = 0
        name_index = 0
        latitude_index = 0
        longitude_index = 0
        comment_index = 0
        marker_index = 0
        size_index = 0
        color_index = 0
        for row in csv_reader:
            if line_count == 0:
                for index, el in enumerate(row):
                    if "ID" in el:
                        id_index = index
                    elif "Name" in el:
                        name_index = index
                    elif "Breitengrad" in el:
                        latitude_index = index
                    elif "Längengrad" in el:
                        longitude_index = index
                    elif "Kommentar" in el:
                        comment_index = index
                    elif "Marker" in el:
                        marker_index = index
                    elif "Größe" in el:
                        size_index = index
                    elif "Farbe" in el:
                        color_index = index
            elif len(row[0]) > 0:
                feature = Feature(row[id_index], row[name_index], row[latitude_index], row[longitude_index], row[comment_index], row[marker_index], row[size_index], row[color_index])
                features.append(feature)
                count += 1
            line_count += 1

    print(f'{count} Features wurden geladen und verarbeitet.')
    return features


def load_json():
    file_type = '*.geojson'
    path = easygui.fileopenbox(default=file_type, filetypes=file_type, title='Laden der GeoJson hinzufügen der Features')
    if path is None or not path.lower().endswith(('.json', '.geojson')):
        print('wrong file type')
        return False

    with open(path, 'r') as file:
        data = json.load(file)
        return data


def save_json(data):
    type = "Ergebnis.geojson"
    path = easygui.filesavebox(filetypes=type, default=type, title='Speichern der Geojson Datei')
    if path is None or not path.lower().endswith(('.json', '.geojson')):
        print('wrong file type')
        return False

    with open(path, 'w') as output_file:
        json.dump(data, output_file, indent=4)


def append_features(data, features):
    for feature in features:
        data['features'].append(feature.get_dict())

    save_json(data)
