# Replace the union method you added to Int_set by a method that allows
# clients of Int_set to use the ­+ operator to denote set union.

    def __add__(self, other):
        new_set = self
        for i in other.get_members():
            new_set.insert(i)
        return new_set
