class AgeExceptionError(Exception):
    """Custom exception for age-related errors."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MyFirstClass:
    """Example class demonstrating various Python features including class variables, instance variables, and custom exceptions."""

    CLASS_VARIABLE = "I am a class variable" # This is a class variable shared by all instances
    MAX_AGE = 120  # Constant for maximum age

    def __init__(self, name):
        self.name = name # This is an instance variable unique to each instance
        self.instance_variable = self.name + " is an instance variable"
        self.age = None  # Initialize age as None

    def __str__(self):
        if hasattr(self, "greeted"):
            return f"{self.name} has already been greeted."
        return f"{self.name} has not been greeted yet."

    def __eq__(self, other):
        """Check equality based on the age."""
        return isinstance(other, MyFirstClass) and self.age == other.age

    def __le__(self, other):
        """Check if this instance is less than another based on age."""
        if not isinstance(other, MyFirstClass):
            return NotImplemented
        if self.age is None or other.age is None:
            return False
        return self.age <= other.age

    def __lt__(self, other):
        """Check if this instance is less than another based on age."""
        if not isinstance(other, MyFirstClass):
            return NotImplemented
        if self.age is None or other.age is None:
            return False
        return self.age < other.age

    def __repr__(self):
        """Return a string representation of the instance."""
        return f"MyFirstClass(name={self.name}, age={self.age})"

    def __setattr__(self, name, value):
        """Custom setter to handle instance variable assignment."""
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

    def greet(self) -> str:
        """Greet the person by name."""
        self.greeted = True
        return f"Hello, {self.name}!"

    def repeat(self, times: int) -> str:
        """
        Repeat the name a given number of times.

        Args:
            times (int): Number of times to repeat the name.

        Returns:
            str: The name repeated the specified number of times.

        """
        return (self.name + " ") * times

    def __check_age(self, age):
        if age < 0:
            message = "You can't be younger than 0."
            raise AgeExceptionError(message)
        if age > self.MAX_AGE:
            message = "I don't think you are older than 120."
            raise AgeExceptionError(message)
        return True

    def input_age(self, age: float) -> str:
        """
        Input age and validate it.

        Args:
            age (float): Age to be validated.

        Returns:
            Confirmation message or error message.

        """
        try:
            self.__check_age(age)
        except TypeError:
            return "Must be number or float."
        except AgeExceptionError as e:
            return e.message
        self.age = age
        return f"{self.name} is {self.age} years old."
