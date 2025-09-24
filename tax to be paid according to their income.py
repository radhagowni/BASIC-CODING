def income_tax(income):
    if income<=300000:
        return "no tax"
    elif (income>300000  and income<=600000):
        res=income-300000
        tax=(res*5)/100
        return tax
    elif(income>600000  and  income<=900000):
        res=income-300000
        tax=(res*5)/100
        res1=res-300000
        tax1=(res*10)/100
        return tax+tax1
    elif(income>900000  and  income<=1200000):
        res=income-300000
        tax=(res*5)/100
        res1=res-300000
        tax1=(res*10)/100
        res2=res1-300000
        tax2=(res2*15)/100
        return tax+tax1+tax2
    elif(income>1200000  and  income<=1500000):
        res=income-300000
        tax=(res*5)/100
        res1=res-300000
        tax1=(res*10)/100
        res2=res1-300000
        tax2=(res2*15)/100
        res3=res2-300000
        tax3=(res3*20)/100
        return tax+tax1+tax2+tax3
    else:
        res=income-300000
        tax=(res*5)/100
        res1=res-300000
        tax1=(res*10)/100
        res2=res1-300000
        tax2=(res*15)/100
        res3=res2-300000
        tax3=(res3*20)/100
        res4=res3-300000
        tax4=(res4*30)/100
        return tax+tax1+tax2+tax3+tax4
income=int(input("Enter your income:"))
m=income_tax(income)
print(m)
    
