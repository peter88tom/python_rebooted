L = [False, False, True, False]
M = []
for item in L:
    if item == True:
        break
    else:
        M.append(item)
        pass
else:
    M = L 

print(M)