import pandas as pd
import requests

# Can use auth parameter for authenticated URLs
r = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)',
                 auth=('john', 'johnspassword'))
tables = pd.read_html(r.text)
print('Tables found:', len(tables))
df1 = tables[0]
print('First Table')
print(df1.head())