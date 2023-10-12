import sys
import os

param_name = os.getenv('param_name')
param_name = sys.argv[0] 
#print("param_name is " + param_name)

# Process the parameter value
processed_data = param_name.upper()  # Example: Convert to uppercase

# Store the data (e.g., in a file)
with open('output.txt', 'w') as f:
    f.write(processed_data)
