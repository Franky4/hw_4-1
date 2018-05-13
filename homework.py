import pandas as pd
import os


DATA_PATH = f'{os.getcwd()}/names/'


def count_top3(years):
    names_row = ['Name', 'Gender', 'Count']
    names_list = [pd.read_csv(DATA_PATH + 'yob' + str(year) + '.txt', names=names_row) for year in years]
    names_all = pd.concat(names_list)
    names_all2 = names_all.groupby(['Gender', 'Name']).sum()
    names_all2 = names_all2.sort_values(by='Count', ascending=False).head(3)
    names_all2 = names_all2.reset_index()
    return [x for x in names_all2.Name]


def count_dynamics(years):
    names_row = ['Name', 'Gender', 'Count']
    names_list = {year: pd.read_csv(DATA_PATH + 'yob' + str(year) + '.txt', names=names_row) for year in years}
    names_all = pd.concat(names_list, names=['Year'])
    del names_all['Name']
    names_all = names_all.groupby(['Gender', 'Year']).sum()
    names_all = names_all.reset_index()
    names_all = names_all.sort_values(by=['Gender', 'Year'], ascending=True)
    del names_all['Year']

    f = []
    m = []
    my_dict = {}

    # for x in names_all.values:
    #     if x[0] == 'F':
    #         f.append(x[1])
    #         my_dict[x[0]] = f
    #     elif x[0] == 'M':
    #         m.append(x[1])
    #         my_dict[x[0]] = m

    for key in set([key[0] for key in names_all.values]):
        my_dict[key] = [value[1] for value in names_all.values if value[0] == key]

    return my_dict


print(count_top3([1900, 1950, 2000]))

print(count_dynamics([1900, 1950, 2000]))