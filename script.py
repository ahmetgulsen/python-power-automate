import sys
import json

# Accept input from the command line (passed by GitHub Actions)
input_data = json.loads(sys.argv[1])

# Example processing: return a greeting
name = input_data.get('name', 'Guest')
result = {"greeting": f"Hello, {name}!"}

# Output the result in JSON format (this will be picked up by GitHub Actions)
print(json.dumps(result))
