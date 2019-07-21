import unittest
from parsing import parse_ingredient

class TestIngredientParsing(unittest.TestCase):

    def test_basic(self):
        string = "onions"
        parsed = { "base_ingredient": "onions"}
        self.assertDictEqual(parse_ingredient(string), parsed)

        string = "5 onions"
        parsed = { "quantity": 5.0, "base_ingredient": "onions"}
        self.assertDictEqual(parse_ingredient(string), parsed)

    def test_fractions(self):
        string = "1/2 onions"
        parsed = { "quantity": .5, "base_ingredient": "onions"}
        self.assertDictEqual(parse_ingredient(string), parsed)

        string = "3 1/2 onions"
        parsed = { "quantity": 3.5, "base_ingredient": "onions"}
        self.assertDictEqual(parse_ingredient(string), parsed)

    def test_standard_units(self):
        string = "1 cup flour"
        parsed = { "quantity": 1.0, "unit":{"type": "standard", "name": "cup"}, "base_ingredient": "flour"}
        self.assertDictEqual(parse_ingredient(string), parsed)

        string = "5 cups flour"
        parsed = { "quantity": 5.0, "unit":{"type": "standard", "name": "cup"}, "base_ingredient": "flour"}
        self.assertDictEqual(parse_ingredient(string), parsed)

        string = "2 1/4 cups flour"
        parsed = { "quantity": 2.25, "unit":{"type": "standard", "name": "cup"}, "base_ingredient": "flour"}
        self.assertDictEqual(parse_ingredient(string), parsed)

    




    

if __name__ == '__main__':
    unittest.main()