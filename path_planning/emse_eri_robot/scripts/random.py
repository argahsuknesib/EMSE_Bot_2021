x = 2.5
y = 2.8

if x - int(x) == 0.5:
        x = x
elif x - int(x) > 0.5 or x - int(x) < 0.5:
        x = round(x)
    
if y - int(y) == 0.5:
        y = y
elif y - int(y) > 0.5 or y - int(y) < 0.5:
        y = round(y)

print(x)
print(y)