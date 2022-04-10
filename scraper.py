from recipe_scrapers import scrape_me


def hello_world(request):
  scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
  scraper.title()
  scraper.total_time()
  scraper.yields()
  scraper.ingredients()
  scraper.instructions()
  scraper.image()
  scraper.host()
  scraper.links()
  scraper.nutrients()

  request_json = request.get_json()
  if request.args and 'message' in request.args:
    return request.args.get('message')
  elif request_json and 'message' in request_json:
    return request_json['message']
  else:
    return f'Hello World!'