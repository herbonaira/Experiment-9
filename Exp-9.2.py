import pandas as pd

md = {'Box': ['Box1','Box1','Box1','Box2','Box2','Box2'], 'Dimension' : ['Length','Width','Height','Length','Width','Height'],
      'Value': [6,4,2,5,3,4]}
messy = pd.DataFrame(md, columns = ['Box','Dimension','Value'])
tidy = messy.pivot_table(index=['Box'], columns = 'Dimension',values = 'Value' )
volume = tidy['Volume'] = tidy.Length*tidy.Width*tidy.Height.rename(columns={0:'Volume'})