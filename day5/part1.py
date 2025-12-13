# import text file, split it on 2 new lines
def load_ranges_and_ingredients(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        input = f.read().split('\n\n')
        ranges = input[0]
        ingredients = input[1]

    return ranges, ingredients

# for each ingredient, check if it is greater than the min, or less than the max of any range
def compare_ingredients_to_ranges(ranges, ingredients):
    for ingredient in ingredients.split('\n'):
        ingredient_value = int(ingredient)
        for line in ranges.split('\n'):
            range_start, range_end = map(int, line.split('-'))
            if range_start <= ingredient_value <= range_end:
                yield ingredient_value
                break

ranges, ingredients = load_ranges_and_ingredients('day5/input_data/input-data.txt')
fresh_ingredients = list(compare_ingredients_to_ranges(ranges, ingredients))
count = len(fresh_ingredients)
print(f'Number of fresh ingredients: {count}')