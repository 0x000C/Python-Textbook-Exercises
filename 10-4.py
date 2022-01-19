# Add to Grades a generator that meets the specification

    def get_students_above(self, grade):
        """Return the students a mean grade > g one at a time"""
        for s in self._students:
            if sum(s.get_grades()) / len(s.get_grades()) > grade:
                yield s
