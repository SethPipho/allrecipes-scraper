from collections import namedtuple
from lxml import html
import re

Recipe = namedtuple("Recipe", ['title','url', 'rating', 'numreviews', 'ingredients', 'instructions'])

def parse_recipe(page:str):
    ''' parses recipe from allrecipes e.g. https://www.allrecipes.com/recipe/13477/double-layer-pumpkin-cheesecake/ '''
    try:
      return parse_format1(page)
    except:
      pass
    
    return parse_format2(page)

  

def parse_format1(page:str):
  ''' parses recipe in format 1 (see testfiles/format1_1.html) for example '''
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

def parse_format2(page:str):
  ''' parses recipe in format 1 (see testfiles/format2_1.html) for example '''

  root = html.fromstring(page)

  title = root.xpath('.//div[@class="intro article-info"]/h1')[0].text
  url = root.xpath('.//link[@rel="canonical"]')[0].attrib.get("href")
  ingredient_tags = root.xpath('.//span[@class="ingredients-item-name"]')
  ingredients = [re.sub(' +', ' ', x.text.strip()) for x in ingredient_tags]
  instruction_tags = root.xpath('.//ul[@class="instructions-section"]//div[@class="section-body"]/p')
  steps = [x.text.strip() for x in instruction_tags if len(x.text) > 0]
  instructions = "\n".join(steps)
  rating = root.xpath('.//meta[@name="og:rating"]')[0].attrib.get("content")
  numreviews = root.xpath('.//div[@class="component recipe-reviews container-full-width template-two-col with-sidebar-right hidden"]')[0].attrib.get("data-ratings-count")

  

  return Recipe(title=title, url=url, rating=rating, numreviews=numreviews, ingredients=ingredients, instructions=instructions)

