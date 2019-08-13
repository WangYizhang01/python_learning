from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_code):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name == country_code:
            return code
    return None

# print(get_country_code("Andorra"))
# print(get_country_code("United Arab Emirates"))
# print(get_country_code("Afghanistan"))