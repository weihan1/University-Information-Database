from typing import List

w = open("website_for_universities", "r")
a = w.readlines()

# Creating a double list; a list of lists of each school and its characteristics
for i in range(0, 145):
    a[i] = a[i].split(",", maxsplit=6)

# Creating a list of all schools
lst = []
for element in a:
    lst.append(element[1])


class University:
    """A Canadian University

    === Attributes ===
    name: the name of the University.
    characteristics: characteristics of the University.

    === Sample Usage ===
    >>> u = University("UofT")
    >>> u.name
    "UofT"
    """

    name: str
    characteristics: List[object]

    def __init__(self, name: str) -> None:
        """Initialize the class University
        >>> u = University("UofT")
        >>> u.name
        "UofT"
        """
        self.name = name
        self.characteristics = []

    def add_characteristics(self, specific_characteristic: str) -> None:
        """Add characteristics to the University
        >>> u = University("University of Toronto")
        >>> u.add_characteristics("Fact")
        >>> u.characteristics()
        U of T's halls have echoed with the debates of future premiers and prime
        ministers. It is famous for research on insulin, bone-marrow
        transplants and regenerative medicine, and for pioneering work in
        artificial intelligence."
        """
        # Determine the index of the school
        ind = lst.index(self.name)
        location = a[ind]

        if specific_characteristic == "Website":
            self.characteristics.append(location[2])
        elif specific_characteristic == "Number of students":
            self.characteristics.append(location[3])
        elif specific_characteristic == "World Ranking":
            self.characteristics.append(location[4])
        elif specific_characteristic == "Province":
            self.characteristics.append(location[5])
        elif specific_characteristic == "Fact":
            self.characteristics.append(location[6])


def final_return(name: str, char: str) -> str:
    """Given the name of the school and its characteristics,
    return its characteristics.

    >>> u = University("Algonquin College")
    >>> u.add_characteristics("Fact")
    >>> final_return("Algonquin College", "Fact")
    "Algonquin College is a  leader on social media as one of the first
    Canadian colleges to use social networking to support student success
    and recruitment."
    """
    if name not in lst:
        return "Not a valid Canadian school. Make sure your " \
               "capitalization and your spelling is correct"
    u = University(name)
    indx = lst.index(name)
    location = a[indx]
    if char == "Website":
        return location[2]
    elif char == "Number of students":
        return location[3]
    elif char == "World Ranking":
        return location[4]
    elif char == "Province":
        return location[5]
    elif char == "Fact":
        return location[6]
    else:
        return "Please enter a valid entry"
