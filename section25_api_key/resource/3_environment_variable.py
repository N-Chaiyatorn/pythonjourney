import os

# use export command in terminal to create environment variable
# example: api_key=test

api_key = os.environ.get("api_key")

print(api_key)

# bonus, other api: https://apilist.fun/