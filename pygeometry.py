inv = "Invalid Input(s)"

def rectpy(type_,**others):
    alist = []
    for i,j in others.items():
        alist.append(j)

    if type_.lower() == 'perimeter':
        return round(2*(alist[0] + alist[1]))

    elif type_.lower() == 'area':
        return round(alist[0]* alist[1],4)
    
    elif type_.lower() == 'diagonal':
        n = (alist[0]**2 + alist[1]**2)**(1/2)
        return round(n, 4)
    else:
        return inv

def squarepy(type_, side):
    if type_.lower() == 'perimeter':
        return round(4*side, 3)
    elif type_.lower() == 'area':
        return round(side**2, 3)
    elif type_.lower() == 'diagonal':
        return round((2**(1/2))*side, 4)
    else:
        return inv
pi = 3.1415

def circlepy(type_, radius):
    if type_.lower() == 'circum' or type_.lower() == 'circumference':
        return round(pi*2*radius, 3)
    elif type_.lower() == 'area':
        return round(pi*(radius**2),3)
    else:
        return inv

def trianglepy(type_, **kwargs):
    """
    Note that for area, the height and breadth are to be given.
    For Area, it should be as follows, a = height, b = breadth
    For perimeter, it should be as follows, a = num, b= num = c = num"""
    blist = []
    for i,j in kwargs.items():
        blist.append(j)

    if type_.lower() == 'area':
        return round(blist[0]*blist[1]*1/2, 3)   
    if type_.lower() == 'perimeter':
        return round(blist[0] + blist[1] + blist[2],3)

def parapy(type_, **kwargs):
    """
    requesting not to use this a lot, still under development!"""
    alist = []
    for i,j in kwargs.items():
        alist.append(j)

    if type_.lower() == 'area':
        return alist[0]*alist[1]

    if type_.lower() == 'base':
        return (alist[0]/2) - alist[1]
    
    if type_.lower() == 'height':
        return alist[0]/alist[1]
    
    if type_.lower() == 'perimeter':
        return 2*(alist[0] + alist[1])

    if type_.lower() == 'side':
        return (alist[0]/2) - alist[1]

def hexapy(type_ , side, perimeter, area):
    if type_.lower() == 'side':
        if perimeter != None:
            return perimeter/6
        elif area != None:
            return (2*(area/9))*(3**(1/4))
        else:
            return inv
        

    elif type_.lower() == 'perimeter':
        if side != None:
            return 6*side
        else:
            return inv
        
    elif type_.lower() == 'area':
        if side != None:
            return ((3**1/3)/2)*(side**2)
        else:
            return inv

    else:
        return inv

def septapy(type_, side, perimeter, area):
    if type_.lower() == 'side':
        if perimeter != None:
            return perimeter/7
        
        elif area != None:
            tan = 0.4815746188
            b = (((4/7)*area*tan)**1/2)
            return b

    elif type_.lower() == 'area':
        if side != None:
            cot = 2.076521397
            a = ((7/4)*(area**2))*cot
            return a    