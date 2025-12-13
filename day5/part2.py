import pandas as pd

def load_ranges_and_ingredients(file_path: str) -> str:
    with open(file_path, 'r') as f:
        ranges = f.read()
    return ranges

def convert_ranges_to_dataframe(id_ranges):
    range_list = []
    for line in id_ranges.split('\n'):
        if not line.strip():
            continue
        range_start, range_end = map(int, line.split('-'))
        range_list.append({'range_start': range_start, 'range_end': range_end})
    df = pd.DataFrame(range_list)
    return df

def merge_ranges(df):
    merged = []
    for _, row in df.sort_values('range_start').iterrows():
        if not merged or row['range_start'] > merged[-1][1] + 1:
            merged.append([row['range_start'], row['range_end']])
        else:
            merged[-1][1] = max(merged[-1][1], row['range_end'])
    return merged

ranges = load_ranges_and_ingredients('day5/input_data/input-data.txt')
df_ranges = convert_ranges_to_dataframe(ranges)

merged_ranges = merge_ranges(df_ranges)
total_fresh_ingredients = sum(end - start + 1 for start, end in merged_ranges)

print(f'Total fresh ingredients: {int(total_fresh_ingredients)}')
