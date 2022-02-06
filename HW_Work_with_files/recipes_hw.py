def get_ingredients(f, number_of_ingredients):
  keys = ["ingredient_name", "quantity", "measure"]
  dish_ingredients_list = []
  for i in range(number_of_ingredients):
    values = f.readline().strip().split(" | ")
    values[1] = int(values[1])
    dish_ingredients_list.append(dict(zip(keys, values)))
  return dish_ingredients_list

cook_book = {}
recipe_file = "recipes.txt"
with open(recipe_file, encoding="utf-8") as f:
  for line in f:
    line = line.strip()
    if not line.isdigit():
      dish = line
    else:
      cook_book[dish] = get_ingredients(f, int(line))
      f.readline()

print("Задача №1 / Вывод на печать словаря cook_book")
for key, value in cook_book.items():
  print("-> Блюдо:", key, "\nИнгредиенты:", value)

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      ingredient_name = ingredient["ingredient_name"]
      ingredient_details = {}
      ingredient_details["measure"] = ingredient["measure"]
      ingredient_details["quantity"] = person_count * int(ingredient["quantity"])
      if ingredient_name in list(shop_list.keys()):
        ingredient_details["quantity"] += shop_list[ingredient_name].get("quantity", 0)
      shop_list[ingredient_name] = ingredient_details
  for key, value in shop_list.items():
    print("Продукт:", key, "  Ед./Кол-во:", value)

print()
print("Задача №2 / Вывод на печать словаря shop_list")
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)