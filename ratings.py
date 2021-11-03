import begin_etl
import pandas as pd
newsRatings = pd.DataFrame()
con = sqlite3.connect('Data.db')
curr = con.cursor()
curr.execute('''CREATE TABLE IF NOT EXISTS BestNewsRating (News text, Bias text, Agree_Ratio real);''')
curr.commit()
for row in curr.execute('SELECT News, bias, ratio FROM NewsBias ORDER BY ratio DESC'):
    newsRatings = pd.concat([newsRatings, pd.DataFrame([[row[0], row[1], row[2]]])], axis=0)
    curr.execute('''INSERT OR IGNORE INTO BestNewsRating VALUES (?, ?, ?)''', [row[0], row[1], row[2]])
    curr.commit()
con.close()
newsRatings.columns = ['News', 'Bias', 'Agree_Ratio']
