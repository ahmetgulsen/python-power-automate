import sys
import json

# Check if there's any input
if len(sys.argv) > 1 and sys.argv[1]:
    input_data = json.loads(sys.argv[1])  # Parse the input
else:
    input_data = {"name": "Guest"}  # Default value in case no input is provided

# Example processing: return a greeting
name = input_data.get('name', 'Guest')
result = {"greeting": f"Hello, {name}!"}

# Output the result in JSON format (this will be picked up by GitHub Actions)
print(json.dumps(result))
