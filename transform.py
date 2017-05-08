import json
import csv

def get_zip_code_geom(geojson, zip_code):
    for feature in geojson['features']:
        if feature['properties']['CODE'] == zip_code:
            return feature['geometry']
    raise Exception('Could not find geometry for `{}` zip code'.format(zip_code))

def get_ct_geom(geojson, ct):
    for feature in geojson['features']:
        if feature['properties']['GEOID10'] == ct:
            return feature['geometry']
    raise Exception('Could not find geometry for `{}` census tract'.format(ct))

with open('./data/bll_counts_and_rate_by_zip_2015_04202017.csv') as data_file:
    with open('./data/bll_counts_and_rate_by_zip_2015_04202017_geocoded.csv', 'w') as data_file_out:
        with open('./data/Zipcodes_Poly.geojson') as geojson_file:
            zip_codes = json.load(geojson_file)
            reader = csv.reader(data_file)
            writer = csv.writer(data_file_out)

            # header
            header_row = next(reader)
            writer.writerow(header_row)

            for row in reader:
                geometry = get_zip_code_geom(zip_codes, row[0])
                row.append(json.dumps(geometry))
                writer.writerow(row)

with open('./data/bll_counts_and_rate_by_ct_2013_2015_04202017.csv') as data_file:
    with open('./data/bll_counts_and_rate_by_ct_2013_2015_04202017_geocoded.csv', 'w') as data_file_out:
        with open('./data/Census_Tracts_2010.geojson') as geojson_file:
            census_tracts = json.load(geojson_file)
            reader = csv.reader(data_file)
            writer = csv.writer(data_file_out)

            # header
            header_row = next(reader)
            writer.writerow(header_row)

            for row in reader:
                geometry = get_ct_geom(census_tracts, row[0])
                row.append(json.dumps(geometry))
                writer.writerow(row)
