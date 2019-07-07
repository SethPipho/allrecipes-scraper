from collections import namedtuple
from lxml import html

Recipe = namedtuple("Recipe", ['title','url', 'rating', 'numreviews', 'ingredients', 'instructions'])

def parse_recipe(page:str):
    ''' parses recipe from allrecipes e.g. https://www.allrecipes.com/recipe/13477/double-layer-pumpkin-cheesecake/ '''

    root = html.fromstring(page)

    title = root.xpath('.//h1[@id="recipe-main-content"]')[0].text
    url = root.xpath('.//link[@id="canonicalUrl"]')[0].attrib.get("href")
    ingredient_tags = root.xpath('.//li[@class="checkList__line"]/label[@title]')
    ingredients = [x.attrib.get("title") for x in ingredient_tags]
    instruction_tags = root.xpath('.//span[@class="recipe-directions__list--item"]')
    steps = [x.text.strip() for x in instruction_tags if x.text is not None]
    instructions = "\n".join(steps)
    rating = root.xpath('.//meta[@itemprop="ratingValue"]')[0].attrib.get("content")
    numreviews = root.xpath('.//meta[@itemprop="reviewCount"]')[0].attrib.get("content")

    return Recipe(title=title, url=url, rating=rating, numreviews=numreviews, ingredients=ingredients, instructions=instructions)