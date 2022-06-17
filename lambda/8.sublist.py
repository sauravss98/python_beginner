color1 = [["green", "blue", "orange"], ["black", "white"], ["white", "black", "orange"]]
srt=[sorted(x,key= lambda  x:x[1]) for x in color1]
print(srt)