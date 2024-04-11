import os 

#Get a specific environment variable
api_key = os.environ.get("API_KEY")

# Print the value or handle if its not set
if api_key:
  print(f"API key: {api_key}")
else:
  print("API key not set.")
