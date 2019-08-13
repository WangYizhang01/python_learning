import json
from country_codes import get_country_code

# dict_1 = {
#     "Country Name": "Andorra",
#     "Country Code": "ARB",
#     "Year": "1960",
#     "Value": "96388069"
# }
# list_1 = [dict_1]

filename = "population_data.json"
# with open(filename,'w') as f:
#     json.dump(list_1,f,ensure_ascii=False)
#     f.close()

# 将数据加载到一个列表中
with open(filename,'r') as f:
    pop_data = json.load(f)
    f.close()

for pop_dict in pop_data:
    if pop_dict['Year'] == '1960':
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print('ERROR - ' + country_name)