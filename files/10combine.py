def combine(sample,test,new):
    with open(sample,'r') as s:
        a=s.read()
    with open(test,'r') as t:
        b=t.read()
    with open(new,'w') as n:
        n.writelines(a+b)
combine("sample.txt","test.txt","new.txt")