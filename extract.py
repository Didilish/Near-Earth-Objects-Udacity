"""Extract data on near-Earth objects and close
approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments
provided at the command line, and uses the resulting collections
to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data
    about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # Loading NEO data from the given CSV file.
    coll_neos = []
    with open(neo_csv_path, 'r') as csv_neos:
        neos_reader = csv.DictReader(csv_neos)
        for row in neos_reader:
            diameter = float('nan')
            name = None
            if (row['diameter'] is not '' and row['diameter'] is not None):
                diameter = float(row['diameter'])
            if (row['name'] is not '' and row['name'] is not None):
                name = row['name']
            neo_found = NearEarthObject(designation=row['pdes'], name=name,
                                        diameter=diameter,
                                        hazardous=row['pha'])
            coll_neos.append(neo_found)
    return coll_neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing
    data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # Loading close approach data from the given JSON file.
    cas = []
    with open(cad_json_path, 'r') as infile:
        json_data = json.load(infile)
        for item in json_data['data']:
            des = item[0]
            time = item[3]
            dist = float(item[4])
            vel = float(item[7])  # 7 is relative velocity, 8 is inf velocity
            cas.append(CloseApproach(des, time, dist, vel))
    return cas
