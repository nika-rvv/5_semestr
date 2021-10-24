from DB.tools import tools
from DB.languages import languages
from DB.language_tool import language_to_tool
from operator import itemgetter
def main():
    development_tools_join_languages = [
        {'languages': p, 'tools': d}
        for p in languages
        for d in tools
        if p.development_id == d.id
    ]


    print("_______________________________________")
    print("Д-1")

    d1 = [(x['languages'].id, x['languages'].name, x['languages'].publication_year, x['tools'].name)
    for x in development_tools_join_languages
        if x['languages'].name.find('Swift') != -1
    ]
    for item in d1:
        print(item)

    print("_______________________________________")
    print("Д2")
    # среда разработки со средней датой публикации языка программирования
    tools_sum_dict = {}
    for tool_language_row in development_tools_join_languages:
        tool_name = tool_language_row['tools'].name
        publication_year = tool_language_row['languages'].publication_year
    if tool_name in tools_sum_dict:
        tools_sum_dict[tool_name]['sum'] += publication_year
        tools_sum_dict[tool_name]['count'] += 1
    else:
        tools_sum_dict[tool_name] = {'sum': publication_year, 'count': 1}
    d2 = sorted(
        [(tool_name, tools_sum_dict[tool_name]['sum'] / tools_sum_dict[tool_name]['count'])
         for tool_name in tools_sum_dict
         if tools_sum_dict[tool_name]['count'] != 0],
        key = itemgetter(1),
        reverse = True
    )
    for item in d2:
        print(item)
    print("_______________________________________")
    print("Д3")
    many_to_many = [(d.name, dp.language_id, dp.tool_id)
                    for d in tools
                        for dp in language_to_tool
                            if d.id == dp.language_id]
    development_to_tool_table = [(language_name, publication_year, tool_name)
                                 for language_name, tool_name, development_tool_id in many_to_many
                                 for tool in tools
                                 if tool.id == development_tool_id
                                 ]
    d3 = {}
    for language in languages:
        if language.name.startswith('P'):
            development_tool_of_language = list(filter(lambda i: i[2] == language.name, development_to_tool_table))
            development_tool_name = [x for x, _, _ in development_tool_of_language]
            d3[language.name] = development_tool_name
    print(d3)



if __name__ == '__main__':
    main()