x=2
y=2
f=open("食堂.csv",'r')
data = f.read()
split_data=data.split('\n')
rows=[]
for row in split_data[1:]:
    rows.append(row.split(','))
print(rows)

for row in rows:
    print(row[2])
