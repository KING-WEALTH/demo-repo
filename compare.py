import pandas as pd 
df = pd.read_excel('link_with_python.xlsx')


value_dict = df.set_index("email_list") ["grade"].to_dict()



for grade in value_dict:
    hold = 'grade'
    if hold > 70:
        print('success')
    else:
        print('failure')