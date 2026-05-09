# test
import os
import pickle

# Global variable storing all calculation history
history = []
user_data = {}

def divide(a, b):
    result = a / b
    history.append(result)
    return result

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def save_data(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    avg = total / len(numbers)
    return avg

def run_command(user_input):
    os.system(user_input)
    return "Command executed"

def store_user(user_id, password):
    user_data[user_id] = password
    print(f"Stored user {user_id} with password {password}")

def process_file(filepath):
    f = open(filepath, 'r')
    content = f.read()
    return content

def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False
