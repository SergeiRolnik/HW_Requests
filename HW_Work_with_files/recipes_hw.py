cook_book = {}
keys = ["ingredient_name", "quantity", "measure"]
with open("recipes.txt", encoding="utf-8") as f:
  for line_in_file in f:
    line = line_in_file.strip()
    if line.isdigit():
      number_of_ingredients = int(line)
    else:
      dish_name = line
      dish_ingredients_list = []
      continue
    for i in range(number_of_ingredients):
      values = f.readline().strip().split(" | ")
      values[1] = int(values[1])
      dish_ingredients_list.append(dict(zip(keys, values)))
    cook_book[dish_name] = dish_ingredients_list
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