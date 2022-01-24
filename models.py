"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    
    """
    # Initialize the attributes
    
    def __init__(self, designation, name, diameter = float('nan'), hazardous = False):

        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        
         Parameters
        ----------
        designation: str
        name : str
        diameter: float
        hazardous: Boolean
        
                
        """
        # Information from the arguments passed to the constructor
        # Attributes `designation`, `name`, `diameter`, and `hazardous`.
        
        if designation == '':
            self.designation = None
        else:
            self.designation = designation
        if name == '':
            self.name =  None
        else:
            self.name = name
        if not diameter :
            self.diameter = float('nan')
        else:
            self.diameter = diameter
        if not hazardous:
            self.hazardous = False
        else:
            if hazardous == 'N':
                self.hazardous = False
            else:
                self.hazardous = True
        
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        
        # fullname for this object built using from self.designation and self.name.
        return (self.designation + " (" + self.name + ") ")

    def __str__(self):
        """Return `str(self)`."""
        # A human-readable string representation.
       
        if self.hazardous:
            return f"NEO {self.name} has a diameter of {self.diameter: .3f} km and is potentially hazardous."
        else:
            return f"NEO {self.name} has a diameter of {self.diameter: .3f} km and is not potentially hazardous."
        #return f"A NearEarthObject NEO has name as {self.name} and diameter of {self.diameter} km and is or not hazardous {self.hazardous} ." 

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")

class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    
     A class to represent a close approach to Earth by an NEO.
    ...
    Attributes
    ----------
    _designation
    time
    distance
    velocity
    neo
    
    """
    # Initialising the attributes
    
    def __init__(self, designation, time, distance = float('nan'), velocity = float('nan')):
        self.time = cd_to_datetime(time)
        
        self._designation = designation
        if not distance :
            self.distance = float('nan')
        else:
            self.distance = distance
        if not velocity :
            self.velocity = float('nan')
        else:
            self.velocity = velocity    
        self.neo = None
        
    @property
    def time_str(self):
        return datetime_to_str(self.time)
    def __str__(self):
        return f"At {datetime_to_str(self.time)} a CloseApproach is travelling to earth with distance of {self.distance} au  and velocity of {self.velocity} km/s "
    def __repr__(self):
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")