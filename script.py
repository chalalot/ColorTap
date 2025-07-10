import random

def generate_layout(ranges, default_direction='left'):
    layout = []

    for x, y_entries in ranges.items():
        for y in y_entries:
            if isinstance(y, int):
                layout.append({'x': x, 'y': y, 'direction': default_direction})
            elif isinstance(y, (list, tuple)) and len(y) == 2:
                for i in range(y[0], y[1] + 1):
                    layout.append({'x': x, 'y': i, 'direction': default_direction})
            else:
                raise ValueError(f"Invalid range format for x={x}: {y}")
    
    return layout

def print_layout_js(layout):
    directions = ['left', 'right', 'up', 'down']
    print("const layout = [")
    for item in layout:
        random_direction = random.choice(directions)
        print(f"    {{ x: {item['x']}, y: {item['y']}, direction: '{random_direction}' }},")
    print("];")

# 🧪 Example usage
if __name__ == "__main__":
    ranges = {
        1: [(11, 13)],
        2: [(11, 15), (19, 20)],
        3: [(11, 16), (18, 22)],
        4: [(11, 23)],
        5: [(10, 10), (14, 17), (19, 24)],
        6: [(6, 11), (13, 16), (20, 24)],
        7: [(5, 17), (21, 24)],
        8: [(5, 21)],
        9: [(2, 21)],
        10: [(1, 21)],
        11: [(2, 21)],
        12: [],
        13: [],
        14: [],
        15: [26],
        16: [],
        17: [],
        18: [26, 29],
        19: [],
        20: [],
        21: [26, 29]
    }

    layout = generate_layout(ranges)
    print_layout_js(layout)
