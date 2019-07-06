from lxml import html
from collections import namedtuple

RecipeLink = namedtuple('RecipeLink', ['title', 'link', 'imgsrc'])

def parse_recipelisting(page:str):
    ''' parses allrecipes recipe list e.g https://www.allrecipes.com/recipes/?page=5 '''

    print(html)

    root = html.fromstring(page)
    cards = root.xpath('//article[@class="fixed-recipe-card"]')

    recipelinks = []
    for card in cards:
        title = card.xpath('.//span[@class="fixed-recipe-card__title-link"]')[0].text
        href = card.xpath('.//div[@class="fixed-recipe-card__info"]//a')[0].attrib.get("href")
        imgsrc = card.xpath('.//img[@class="fixed-recipe-card__img"]')[0].attrib.get("data-original-src")

        link = RecipeLink(title=title, link=href, imgsrc=imgsrc)
        recipelinks.append(link)
    
    return recipelinks