#W1D2
pantry = {'pasta': 3, 'garlic': 4,'sauce': 2,
          'basil': 2, 'salt': 3, 'olive oil': 3,
          'rice': 3, 'bread': 3, 'peanut butter': 1,
          'flour': 1, 'eggs': 1, 'onions': 1, 'mushrooms': 3,
          'broccoli': 2, 'butter': 2,'pickles': 6, 'milk': 2,
          'chia seeds': 5}

meal_recipe = {'pasta': 2, 'garlic': 2, 'sauce': 3,
          'basil': 4, 'salt': 1, 'pepper': 2,
          'olive oil': 2, 'onions': 2, 'mushrooms': 6}


shopping_list = dict()

for itme in meal_recipe
    try:
        if meal_recipe[item] > pantry[item]:
            shopping_list[item] = meal_recipe[item] - pantry[item]
    except:
        shopping_list[item] meal_recipe[item]



