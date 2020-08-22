
from datetime import time
import requests
import json
r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

package_name = packages_json[0]['name']
package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

r=requests.get(package_url)
package_json = r.json()

package_str = json.dumps(package_json,indent=2)
#print(package_str)

installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

print(package_name, installs_30, installs_90, installs_365)
data = {
    'name': package_name,
    'analytics':{
        '30d':installs_30,
        '90d':installs_90,
        '365d':installs_365
    },
    'timetosleep':  r.elapsed.total_seconds()
}
timetosleep = r.elapsed.total_seconds()
print(data)
print(timetosleep)

with open('package_info.json','w') as f:
    json.dump(data, f, indent=2)
