from ast import pattern
import re


def end(text):
    x=re.search("main\Z",text)
    print(x)
    if x:
        print("Found")
    else:
        print("Not found")

end("Tasfdaf ai main")
end("safd jajfn ka fas f")
end("fa snjn main dsafkjanj n as ")