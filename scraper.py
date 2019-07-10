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
page = 1626
count = 0

OUTPUT_PATH = "data/recipes-raw.jsonl"
output_file = open(OUTPUT_PATH, "a", encoding="utf-8")

while True:
    url = RECIPE_LIST_URL.format(page=str(page))
    r = fetch(url)
    if r.status_code == 404:
        break
    print("Page:", page)
    page += 1
    
    recipelisting = recipelist.parse_recipelisting(r.text)

    for listing in recipelisting:
        count += 1
        r = fetch(listing.link)
        if r.status_code != 200:
            print("fetch error:", listing.link)
            continue
        parsed = recipe.parse_recipe(r.text)
        if parsed is None:
            print("parse error:", listing.link)
            continue
        parsed_dict = parsed._asdict()
        parsed_dict["imgsrc"] = listing.imgsrc

        json_output = json.dumps(parsed_dict, ensure_ascii=False)
        output_file.write(json_output + "\n")
        output_file.flush()
       
    
        
print("Done!")
print("Found", count, "recipes")
output_file.close()
