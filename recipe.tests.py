import unittest
import recipe

class TestRecipeParse(unittest.TestCase):

    def test_parse_recipe(self):

        self.maxDiff = None

        testfile = open("testfiles/recipenew.html", encoding="utf-8").read()
        parsed_recipe = recipe.parse_recipe(testfile)

        recipe1 = recipe.Recipe(
            title= "Double Layer Pumpkin Cheesecake",
            url= "https://www.allrecipes.com/recipe/13477/double-layer-pumpkin-cheesecake/",
            rating="4.77",
            numreviews="2786",
            ingredients=[
                "2 (8 ounce) packages cream cheese, softened",
                "1/2 cup white sugar",
                "1/2 teaspoon vanilla extract",
                "2 eggs",
                "1 (9 inch) prepared graham cracker crust",
                "1/2 cup pumpkin puree",
                "1/2 teaspoon ground cinnamon",
                "1 pinch ground cloves",
                "1 pinch ground nutmeg",
                "1/2 cup frozen whipped topping, thawed"
            ],
            instructions = 
                ('Preheat oven to 325 degrees F (165 degrees C).\n'
                'In a large bowl, combine cream cheese, sugar and vanilla. Beat until smooth. Blend in eggs one at a time. Remove 1 cup of batter and spread into bottom of crust; set aside.\n'
                'Add pumpkin, cinnamon, cloves and nutmeg to the remaining batter and stir gently until well blended. Carefully spread over the batter in the crust.\n'
                'Bake in preheated oven for 35 to 40 minutes, or until center is almost set. Allow to cool, then refrigerate for 3 hours or overnight. Cover with whipped topping before serving.')
        )


        self.assertEqual(parsed_recipe.title, recipe1.title)
        self.assertEqual(parsed_recipe.url, recipe1.url)
        self.assertEqual(parsed_recipe.ingredients, recipe1.ingredients)
        self.assertEqual(parsed_recipe.instructions, recipe1.instructions)
        self.assertEqual(parsed_recipe.rating, recipe1.rating)
        self.assertEqual(parsed_recipe.numreviews, recipe1.numreviews)



    

if __name__ == '__main__':
    unittest.main()