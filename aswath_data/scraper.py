import pandas as pd
import requests



data = pd.read_html('https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histimpl.html')

print(data)




print('done')