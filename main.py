import re
def solve(ex):
    #ex=input ("Enter expression: ")
    ex = re.sub(r"\s+", "", ex, flags=re.UNICODE)
    su=ex.split("+")
    sum=0
    for i in range(len(su)):
        di=su[i].split("-")
        diff=0
        for j in range(len(di)):
            pr=di[j].split("*")
            pro=1
            for k in range(len(pr)):
                qo=pr[k].split("/")
                qou=1
                for l in range(len(qo)):
                    if l == 0:
                        qou *= float(qo[l])
                    else:
                        qou /= float(qo[l])
                pro*=float(qou)
            if j==0:
                diff+=float(pro)
            else :
                diff=diff-float(pro)
        sum=sum+float(diff)
    if sum==int(sum):
        return int(sum)
    else:
        return sum
            



