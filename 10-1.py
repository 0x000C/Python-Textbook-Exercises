# Add a method satisfying the specification below to the Int_set class.

    def union(self, other):
        """other is an Int_set
            mutates self so that it contains exactly the elemnts in self
            plus the elements in other."""
        for i in other.get_members():
            self.insert(i)
