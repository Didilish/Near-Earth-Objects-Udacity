"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from helpers import datetime_to_str

def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # TODO: Write the results to a CSV file, following the specification in the instructions.

    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)
   
        for result in results:
            date = datetime_to_str(result.time)
            distance = result.distance
            velocity = result.velocity
            designation = result._designation
            name = result.neo.name
            diameter = result.neo.diameter 
            hazardous = result.neo.hazardous
            neo = [date, distance, velocity, designation, name, diameter, hazardous]
            writer.writerow(neo)
            
def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.
    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
 
    # Following the specification in the instructions, writing the results to a JSON file.

    clap_fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'neo')
    neo_fieldnames = ('designation', 'name', 'diameter_km', 'potentially_hazardous')
    
    output = list()
    
    
    with open(filename, 'w') as outfile:
        for result in results:
            date = datetime_to_str(result.time)
            distance = float(result.distance)
            velocity = float(result.velocity)
            designation = str(result.neo.designation)
            name = '' if result.neo.name is None else result.neo.name
            diameter = float(result.neo.diameter)
            hazardous = result.neo.hazardous
            neo_data = (designation, name, diameter, hazardous)
            neo_dict = dict(zip(neo_fieldnames, neo_data))
            clap_data = (date, distance, velocity, neo_dict)
            clap_dict = dict(zip(clap_fieldnames, clap_data))
            
            output.append(clap_dict)
        json.dump(output, outfile, indent=2)