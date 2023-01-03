import math
def similar_triangles(coords_1, coords_2) -> bool:
    first_tri=[]
    for j in range(2):
        degrees=[]
        for i in range(3):
            if i ==2:
                i=-1
            if j==0:
                x1=coords_1[i][0]
                x2=coords_1[i+1][0]
                y1=coords_1[i][1]
                y2=coords_1[i+1][1]
            else:
                x1=coords_2[i][0]
                x2=coords_2[i+1][0]
                y1=coords_2[i][1]
                y2=coords_2[i+1][1]
            # print((x2 - x1)**2 )
            # print((y2 - y1)**2 )
            # print(math.sqrt(((x2 - x1)**2)+(y2 - y1)**2))
            degrees.append(math.sqrt(((x2 - x1)**2)+(y2 - y1)**2))

        a=degrees[0]
        b=degrees[1]
        c=degrees[2]

        a2=math.pow(degrees[0],2)
        b2=math.pow(degrees[1],2)
        c2=math.pow(degrees[2],2)

        alpha = math.acos((b2+c2-a2)/(2*b*c))
        betta = math.acos((a2+c2-b2)/(2*a*c))
        gamma = math.acos((a2+b2-c2)/(2*a*b))

        alpha=round(alpha*180/math.pi)
        betta= round(betta *180/math.pi)
        gamma=round(gamma*180/math.pi)
        if j==0:
            first_tri.append(alpha)
            first_tri.append(betta)
            first_tri.append(gamma)
        else:
            if first_tri.count(alpha)!=0 and first_tri.count(betta)!=0 and first_tri.count(gamma)!=0:
                return True


        print(alpha)
        print(gamma)
        print(betta)



    return False
similar_triangles([(-3,-2), (-4, 2), (-3, -1)], [(4, -10), (9, 10), (9, 5)])