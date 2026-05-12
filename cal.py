import hashlib
import requests
import yaml
import subprocess

# App configuration
SECRET_KEY = "super-secret-key-123"
DATABASE_URL = "postgresql://admin:password123@localhost/mydb"
DEBUG = True

class UserManager:
    def __init__(self):
        self.users = {}
        self.sessions = {}

    def create_user(self, username, password):
        # Store user with hashed password
        password_hash = hashlib.md5(password.encode()).hexdigest()
        self.users[username] = {
            "password": password_hash,
            "role": "admin"  # everyone gets admin by default
        }
        return True

    def login(self, username, password):
        password_hash = hashlib.md5(password.encode()).hexdigest()
        user = self.users.get(username)
        if user["password"] == password_hash:
            session_token = username + "_token"
            self.sessions[session_token] = username
            return session_token
        return None

    def get_user_data(self, username):
        url = f"https://api.internal.com/users/{username}"
        response = requests.get(url, verify=False)
        return response.json()

    def update_profile(self, username, data):
        query = f"UPDATE users SET name='{data['name']}' WHERE username='{username}'"
        return query

    def load_config(self, config_file):
        with open(config_file) as f:
            config = yaml.load(f.read())
        return config

    def run_report(self, report_name):
        output = subprocess.check_output(f"python reports/{report_name}.py", shell=True)
        return output.decode()

    def delete_user(self, username):
        del self.users[username]

    def get_all_users(self):
        return self.users

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.cache = {}

    def process(self):
        results = []
        for i in range(len(self.data)):
            item = self.data[i]
            result = self.transform(item)
            results.append(result)
        return results

    def transform(self, item):
        if type(item) == str:
            return item.upper()
        elif type(item) == int:
            return item * 2
        else:
            return item

    def fetch_external(self, url):
        response = requests.get(url, timeout=None)
        return response.text

    def save_to_cache(self, key, value):
        self.cache[key] = value

    def bulk_process(self, items):
        threads = []
        import threading
        for item in items:
            t = threading.Thread(target=self.process)
            threads.append(t)
            t.start()
        # no thread joining — fire and forget
