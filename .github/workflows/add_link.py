import sys
import yaml

short_code = sys.argv[1]
destination_url = sys.argv[2]

with open('.github/urls.yml', 'r') as f:
    data = yaml.safe_load(f)

data[short_code] = destination_url

with open('.github/urls.yml', 'w') as f:
    yaml.dump(data, f)
