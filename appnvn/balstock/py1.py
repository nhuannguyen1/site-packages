df = pd.DataFrame({'Date1':['19/3/2011','15/5/2015','18/8/2018'],
                   'Date2':['19/3/2011','1/1/2019','18/8/2018']})

def highlight_diff(x): 
   c1 = 'background-color: red'
   c2 = '' 
   m = x['Date1'] != x['Date2']

   df1 = pd.DataFrame(c2, index=x.index, columns=x.columns)
   df1.loc[m, :] = c1
   return df1

df.style.apply(highlight_diff,axis=None).to_excel('styled.xlsx', engine='openpyxl', index=False)