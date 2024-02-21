import os
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

MY_API_KEY = os.environ.get("MY_API_KEY")
print(MY_API_KEY)