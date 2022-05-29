import pandas as pd

import scrapefunctions as sf


data = pd.read_html('https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histimpl.html')
df = data[0]

print(df)

# Below code doesn't work for some reason

# base_url = 'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/'
# current_data_url = base_url + 'datacurrent.html'


# soup = sf.get_soup(current_data_url)
# table_soup = soup.find('table')

# print(table_soup)










print('done')