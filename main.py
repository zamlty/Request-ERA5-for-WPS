import requests

auth = ('<UID>', '<API KEY>')
datestr = '1998-06-01/1998-06-03'
timestr = ['%02d:00' % h for h in range(0, 24, 6)]

url_base = 'https://cds.climate.copernicus.eu/api/v2/'
params_common = {
    'date': datestr, 'time': timestr,
    'product_type': 'reanalysis', 'format': 'grib',
    # 'area': [55, 70, 0, 150], # North, West, South, East
}

url_pl = url_base + 'resources/reanalysis-era5-pressure-levels'
params_pl = {
    **params_common,
    'variable': [
        'geopotential', 'relative_humidity', 'temperature',
        'u_component_of_wind', 'v_component_of_wind',
    ],
    'pressure_level': [
        '1', '2', '3',
        '5', '7', '10',
        '20', '30', '50',
        '70', '100', '125',
        '150', '175', '200',
        '225', '250', '300',
        '350', '400', '450',
        '500', '550', '600',
        '650', '700', '750',
        '775', '800', '825',
        '850', '875', '900',
        '925', '950', '975',
        '1000',
    ]
}

url_sc = url_base + 'resources/reanalysis-era5-single-levels'
params_sc = {
    **params_common,
    'variable': [
        '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
        '2m_temperature', 'land_sea_mask', 'mean_sea_level_pressure',
        'sea_ice_cover', 'sea_surface_temperature', 'skin_temperature', 'snow_depth',
        'soil_temperature_level_1', 'soil_temperature_level_2', 'soil_temperature_level_3',
        'soil_temperature_level_4', 'surface_pressure', 'volumetric_soil_water_layer_1',
        'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4',
    ]
}

reqs = {'pl': (url_pl, params_pl), 'sc': (url_sc, params_sc)}

sess = requests.Session()
sess.auth = auth

for k, (url, params) in reqs.items():
    print(k)
    r = sess.post(url, json=params)
    print(r.json())

