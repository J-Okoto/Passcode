import unittest
from code import User

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('J-Okoto','hushpuppy')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'J-Okoto')
        self.assertEqual(self.new_user.password,'hushpuppy01')   