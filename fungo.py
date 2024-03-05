import re
a = "San Francisco-Oakland-Fremont, CA"
print(re.split(', |_|-|!|\+',a))