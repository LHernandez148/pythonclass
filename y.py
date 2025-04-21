i = 0
LOST = []

while i == 0:
    LOI = []
    LOSTT = []
    LOIS = []
    LOIS = list((input("\nInsert the desired seat numbers separated by a comma and a space, 1-4 include a $50 fee, 5-8 are in the emergency aisle: ").split(", ")))
    cost = 0
    p = 0
    e = 0
    D = 0
    m = 0
    z = 0
    v = 0
    b = len(LOIS)
    L = 0
    f = 0
    q = 0
    k = 0
    w = 0

    while v < b:
        LOI.append(int(LOIS[v]))
        v = v + 1

    if LOST == []:
        while f < len(LOI):
            LOST.append(int(LOI[w]))
            w = w + 1
            f = f + 1
    else:
        while p < len(LOI):
            D = 0
            taken = False
            while D < len(LOST):
                if LOI[p] == LOST[D]:
                    print("\n Sorry seat {} is already taken".format(LOI[p]))
                    m = 1
                    taken = True
                    break
                D = D + 1
            if not taken:
                LOSTT.append(LOI[p])
            p = p + 1

    if m == 1:
        print("\n Sorry Try again")
    if m == 0:
        q = 0
        k = 0
        while q < len(LOSTT):
            LOST.append(int(LOSTT[k]))
            q = q + 1
            k = k + 1
        r = 0
        o = 0
        x = 0
        L = 0
        while o < len(LOI):
            if LOI[o] == 1 or LOI[o] == 2 or LOI[o] == 3 or LOI[o] == 4:
                cost = cost + 50
                z = 1
            if LOI[o] == 5 or LOI[o] == 6 or LOI[o] == 7 or LOI[o] == 8:
                L = 1
            o = o + 1
        if L == 1:
            x = 1
            EMGI = input("\nOne of your seats is in the emergency aisle, do you accept all responsibilities that come with this during an emergency, Yes or no? ")
            if EMGI == "Yes" or EMGI == "yes":
                x = 0
        if x == 0:
            cost = cost + (len(LOI) * 100)
            print("\nHere are the seat number(s) selected: {} \nHere is the cost: ${}".format(LOI, cost))
            if z == 1:
                print("With the added $50 fee for every first class ticket")