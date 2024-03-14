class MyComparableKey:
    def __init__(self, int_value, string_value) -> None:
        self.int_value = int_value
        self.string_value = string_value

    def __lt__(self, other) -> bool:
        """Retruns the false if the numeric value is less than the other
        # - If  the values are equal then check if the self sting is less than the
          other string and return True
        """
        if self.int_value < other.int_value:
            return True
        elif self.int_value == other.int_value:
            if self.string_value < other.string_value:
                return True
        return False
