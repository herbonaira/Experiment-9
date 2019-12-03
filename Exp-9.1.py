import pandas as pd

wbb_math = {'Students': ['Ice Bear','Panda','Grizzly'], 'Math': [80,95,79]} 
wbb_elec = {'Students': ['Ice Bear','Panda','Grizzly'], 'Electronics': [85,81,83]} 
wbb_geas = {'Students': ['Ice Bear','Panda','Grizzly'], 'GEAS': [90,79,93]}
wbb_esat = {'Students': ['Ice Bear','Panda','Grizzly'], 'ESAT': [93,89,88]}

math = pd.DataFrame(wbb_math,columns = ['Students', 'Math'])
elec = pd.DataFrame(wbb_elec,columns = ['Students', 'Electronics'])
geas = pd.DataFrame(wbb_geas,columns = ['Students','GEAS'])
esat = pd.DataFrame(wbb_esat,columns = ['Students', 'ESAT'])

mathelec = pd.merge(math, elec, how = 'outer', on ='Students')
mathlecgeas= pd.merge(mathelec, geas, how = 'outer', on = 'Students')
wbb = pd.merge(mathlecgeas, esat, how ='outer', on = 'Students')
long = pd.melt(wbb, id_vars='Students',value_vars=['Math','Electronics','GEAS','ESAT'])