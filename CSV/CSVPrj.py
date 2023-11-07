import pandas as pd
import matplotlib.pyplot as plt

#visualization
csvFile1 = pd.read_csv("injury-statistics-work-related-claims-2018-csv.csv")
x = csvFile1.Year
y = csvFile1.Value
plt.scatter(x, y)
plt.show()

csvFile2 = pd.read_csv("serious-injury-outcome-indicators-2000-2020-CSV.csv")
a = csvFile2.Year
b = csvFile2.Value      
plt.scatter(a, b)
plt.show()


csvFilediff = pd.read_csv("diff.csv")
a = csvFilediff.Year
b = csvFilediff.Value
c = csvFilediff.Year
d = csvFilediff.Value
plt.scatter(a, b)
plt.show()
plt.scatter(c, d)
plt.show()






#merge
df1 = pd.read_csv("Age1.csv")
df2 = pd.read_csv("Age2.csv")
c_result_m = df1.merge(df2, how='outer')
print(c_result_m)



