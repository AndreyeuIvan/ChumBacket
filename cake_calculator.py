def cakes(receipt, ingridients):
    """Calculate how much cakes we can bake"""
    ingridients = {key:receipt[key] - ingridients.get(key,0) for key in ingridients.keys()}
    return ingridients

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
      
