import os, json

DATA_PATH = 'data'

def load_data(file_name):
    """Load products from the JSON file."""
    file_path = os.path.join(DATA_PATH, file_name)
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return json.load(file)
      
def save_data(file_name, data):
    """Save products to the JSON file."""
    file_path = os.path.join(DATA_PATH, file_name)
    try:
      if not os.path.exists(DATA_PATH):
          raise FileNotFoundError(f"Data directory '{DATA_PATH}' does not exist.")
      with open(file_path, 'w') as file:
          json.dump(data, file, indent=4)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise