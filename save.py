import json

def save_options(options, filename='test.json'):
    with open(filename, 'w') as f:
        json.dump(options, f, indent=4)

# 示例选项
options = {
    'option1': 'value1',
    'option2': 'value2',
    'option3': 'value3'
}

# 保存选项
save_options(options)

def load_options(filename='config.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# 加载选项
loaded_options = load_options()
print(loaded_options['option6'])