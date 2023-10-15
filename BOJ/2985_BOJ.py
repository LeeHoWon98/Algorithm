n1, n2, n3 = map(int, input().split())

if n1 + n2 == n3:
    print(str(n1)+"+"+str(n2)+"="+str(n3))
elif n1 - n2 == n3:
    print(str(n1)+"-"+str(n2)+"="+str(n3))
elif n1 * n2 == n3:
    print(str(n1)+"*"+str(n2)+"="+str(n3))
elif n1 // n2 == n3:
    print(str(n1)+"/"+str(n2)+"="+str(n3))
elif n1 == n2 + n3:
    print(str(n1)+"="+str(n2)+"+"+str(n3))
elif n1 == n2 - n3:
    print(str(n1)+"="+str(n2)+"-"+str(n3))
elif n1 == n2 * n3:
    print(str(n1)+"="+str(n2)+"*"+str(n3))
elif n1 == n2 // n3:
    print(str(n1)+"="+str(n2)+"/"+str(n3))