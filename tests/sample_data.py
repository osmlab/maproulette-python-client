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

test_overpassQL_query = '''way["name"="Københavns Lufthavn"];\nout body geom qt;'''

create_challenge_output = json.dumps(
    {'name': 'Test_Challenge_Name',
    'description': 'This is a test challenge',
    'instruction': 'Do something',
    'overpassQL': test_overpassQL_query})

test_project = json.loads('''{"name": "Test_Project_Name",
                           "description": "This is a test project"
                           }'''
                          )
