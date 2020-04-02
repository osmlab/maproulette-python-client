import json

test_geojson = json.loads('''{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": null,
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [
                        -0.13698190844,
                        50.81561190201
                    ],
                    [
                        -0.13702256313,
                        50.81534476302
                    ]
                ]
            }
        }
    ]
}''')

test_overpassQL_query = '''way["name"="Københavns Lufthavn"];
out body geom qt;'''

