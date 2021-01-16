
import os

class Config :

    API_KEY = os.environ.get('API_KEY') if os.environ.get('API_KEY') else '3b1d146f'
