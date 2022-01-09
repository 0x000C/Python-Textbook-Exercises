# Implement a subclass of Person that meets the specification


class Politician(Person):
    """ A politician is a person who can belong to a political party"""

    def __init__(self, name, party=None):
        """name and party are strings"""
        super().__init__(name)
        self._party = party

    def get_party(self):
        """returns the party to which self belongs"""
        return self._party

    def might_agree(self, other):
        """returns True if self and other belong to the same part
             or at least one of then does not belong to a party"""
        if self.get_party() is None or other.get_Party() is None:
            return True
        else
            return self.get_party() == other.get_party()
