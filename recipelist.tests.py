import unittest
import recipelist

class TestRecipeListscrape(unittest.TestCase):

    def test_scrape_recipelist(self):

        testfile = open("testfiles/recipelist.html", encoding="utf-8").read()
        recipe_list = recipelist.scrape_recipelisting(testfile)
        
        self.assertEqual(len(recipe_list), 20)
     
        recipe0 = recipelist.RecipeLink(
                title="Double Layer Pumpkin Cheesecake",
                link="https://www.allrecipes.com/recipe/13477/double-layer-pumpkin-cheesecake/",
                imgsrc="https://images.media-allrecipes.com/userphotos/300x300/303675.jpg"
            )

        recipe19 = recipelist.RecipeLink(
                title =  "Homemade Black Bean Veggie Burgers",
                link = "https://www.allrecipes.com/recipe/85452/homemade-black-bean-veggie-burgers/",
                imgsrc = "https://images.media-allrecipes.com/userphotos/300x300/4548470.jpg"
            )

        self.assertEqual(recipe_list[0], recipe0)
        self.assertEqual(recipe_list[19], recipe19)


    

if __name__ == '__main__':
    unittest.main()