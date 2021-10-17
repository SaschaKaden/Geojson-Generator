import sys
from src import util
from src import feature
import easygui


if __name__ == '__main__':
    features = util.load_csv()
    if not features:
        print("Laden schlug fehl, Programm wird beendet!")
        sys.exit()

    msg = "Sollen die Features zu einer existierenden Datei hinzugefügt werden?"
    choice = easygui.ynbox(msg)
    if choice:
        json_data = util.load_json()
    else:
        json_data = feature.create_feature_collection()
    if not json_data:
        print("Laden schlug fehl, Programm wird beendet!")
        sys.exit()

    util.append_features(json_data, features)

