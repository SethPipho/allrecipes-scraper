import requests
import recipe
import recipelist
import time
import json
import ratelimit

@ratelimit.sleep_and_retry
@ratelimit.limits(calls=1, period=1)
def fetch(url):
    return requests.get(url)

RECIPE_LIST_URL = "https://www.allrecipes.com/recipes/?page={page}"
page = 0

recipes = []

while True:
    url = RECIPE_LIST_URL.format(page=str(page))
    r = fetch(url)
    if r.status_code == 404:
        break
    print("Page:", page)
    page += 1
    
    recipelisting = recipelist.parse_recipelisting(r.text)

    for listing in recipelisting:
        r = fetch(listing.link)
        parsed = recipe.parse_recipe(r.text)
        parsed_dict = parsed._asdict()
        parsed_dict["imgsrc"] = listing.imgsrc
        recipes.append(parsed_dict)
        
print("Done!")
print("Found",len(recipes), "recipes")
with open("data/recipes-raw.json", "w", encoding="utf-8") as f:
    json.dump(recipes, f, ensure_ascii=False, indent=5)
