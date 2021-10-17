def create_feature_collection():
    d = dict({'type': 'FeatureCollection', 'features': []})
    return d


class Feature:
    id = 0
    name = ""
    latitude = 0
    longitude = 0
    comment = ""
    marker = "campsite"
    size = "medium"
    color = "#77777"

    def __init__(self, id_in, name, latitude, longitude, comment, marker, size, color):
        self.id = int(id_in)
        self.name = name
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.comment = comment
        self.marker = marker
        self.size = size
        self.color = color

    def get_dict(self):
        values = dict({'_comment': self.id, 'type': 'Feature',
                       'properties': {'marker-color': self.color, 'fill': '#808080', 'stroke': '#808080',
                                      'marker-size': self.size, 'marker-symbol': self.marker,
                                      'popup-text': str(self.id) + ": " + self.name, 'color': self.color},
                       'geometry': {'type': 'Point', 'coordinates': [self.longitude, self.latitude]}})
        return values
