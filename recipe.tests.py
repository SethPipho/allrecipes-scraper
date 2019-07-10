import unittest
import recipe
import requests

class TestRecipeParse(unittest.TestCase):

    def test_parse_recipe_format_1(self):

        self.maxDiff = None

        testfile = open("testfiles/format1_1.html", encoding="utf-8")
        parsed_recipe = recipe.parse_recipe(testfile.read())
        testfile.close()

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

        testfile = open("testfiles/format1_2.html", encoding="utf-8")
        parsed_recipe = recipe.parse_recipe(testfile.read())
        testfile.close()

        recipe1 = recipe.Recipe(
            title= "Super Moist Zucchini Bread",
            url= "https://www.allrecipes.com/recipe/215488/super-moist-zucchini-bread/",
            rating="2.16",
            numreviews="37",
            ingredients=[
                "3 cups grated zucchini",
                "3 cups all-purpose flour",
                "3 tablespoons ground cinnamon",
                "1 teaspoon baking soda",
                "1 teaspoon baking powder",
                "1 teaspoon salt",
                "1 cup unsweetened applesauce",
                "3 tablespoons vanilla extract",
                "3 eggs",
                "3 tablespoons butter, melted",
                "1 cup chopped walnuts (optional)"
            ],
            instructions = 
                ('Preheat an oven to 325 degrees F (165 degrees C). Grease 2 8x4-inch loaf pans or 2 12-cup muffin pans.\n'
                'Place the zucchini in a strainer and set aside to drain into a bowl or sink.\n'
                'Sift the flour, cinnamon, baking soda, baking powder, and salt together in a large bowl. Create a well in the middle of the flour mixture; combine the applesauce, vanilla, eggs, butter, walnuts, and drained zucchini in the center of the well. Mix until all ingredients are combined into a batter; pour into the loaf pans.\n'
                'Bake the loaves in the preheated oven until a toothpick inserted into the center comes out clean, about 1 hour for loaves or 25 minutes for muffins. Cool in the pans for 10 minutes before removing to cool completely on a wire rack.')
        )

        self.assertEqual(parsed_recipe.title, recipe1.title)
        self.assertEqual(parsed_recipe.url, recipe1.url)
        self.assertEqual(parsed_recipe.ingredients, recipe1.ingredients)
        self.assertEqual(parsed_recipe.instructions, recipe1.instructions)
        self.assertEqual(parsed_recipe.rating, recipe1.rating)
        self.assertEqual(parsed_recipe.numreviews, recipe1.numreviews)

    def test_parse_recipe_format2(self):

        self.maxDiff = None

        testfile = open("testfiles/format2_1.html", encoding="utf-8")
        parsed_recipe = recipe.parse_recipe(testfile.read())
        testfile.close()

        recipe1 = recipe.Recipe(
            title= "Broccoli Cheese Soup",
            url= "https://www.allrecipes.com/recipe/13045/broccoli-cheese-soup/",
            rating="4.61602209944751",
            numreviews="2896",
            ingredients=[
                "½ cup butter",
                "1 onion, chopped",
                "1 (16 ounce) package frozen chopped broccoli",
                "4 (14.5 ounce) cans chicken broth",
                "1 (1 pound) loaf processed cheese food, cubed",
                "2 cups milk",
                "1 tablespoon garlic powder",
                "⅔ cup cornstarch",
                "1 cup water"
            ],
            instructions = 
                ('In a stockpot, melt butter over medium heat. Cook onion in butter until softened. Stir in broccoli, and cover with chicken broth. Simmer until broccoli is tender, 10 to 15 minutes.\n'
                'Reduce heat, and stir in cheese cubes until melted. Mix in milk and garlic powder.\n'
                'In a small bowl, stir cornstarch into water until dissolved. Stir into soup; cook, stirring frequently, until thick.'
            ))

        self.assertEqual(parsed_recipe.title, recipe1.title)
        self.assertEqual(parsed_recipe.url, recipe1.url)
        self.assertEqual(parsed_recipe.ingredients, recipe1.ingredients)
        self.assertEqual(parsed_recipe.instructions, recipe1.instructions)
        self.assertEqual(parsed_recipe.rating, recipe1.rating)
        self.assertEqual(parsed_recipe.numreviews, recipe1.numreviews) 

     #recipe without ratings or reviews broke format 2
    def test_parse_recipe_format_2_unrated(self):

        self.maxDiff = None

        testfile = open("testfiles/format2_unrated.html", encoding="utf-8")
        parsed_recipe = recipe.parse_recipe(testfile.read())
        testfile.close()
        
        self.assertEqual(parsed_recipe.rating, "0")
    
    #test list of urls that failed during initial bulk scraping
    """  def test_errors(self):
        with open('data/errors.txt') as f:
            for row in f:
                url = row.strip()
                r = requests.get(url)
                print(url)
                if (r.status_code != 200):
                    print('fetch error:', url)
                    continue
                parsed = recipe.parse_recipe(r.text)
                if parsed == None:
                    print('parse error:', url) """
              

                
             
        



    

if __name__ == '__main__':
    unittest.main()