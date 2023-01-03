def mountain_scape(tops):
    all_area = 0
    for  tri in range (len(tops)):
        all_area +=0.5*tops[tri][1]*tops[tri][1]*2
        print(0.5*tops[tri][1]*tops[tri][1]*2)
        for i in range(tri+1,len(tops)):
            print(tops[i])
            if (tops[tri][0] + (tops[tri][1])) > (tops[i][0] - tops[i][1]):
                base_overlapping = (tops[tri][0] + tops[tri][1]) - (tops[i][0] - tops[i][1])
                if base_overlapping > tops[i][1]*2:
                    base_overlapping = tops[i][1]*2
                hight_overlapping = base_overlapping/2
                print(0.5*base_overlapping*hight_overlapping,"::",base_overlapping,hight_overlapping)
                all_area -= 0.5*base_overlapping*hight_overlapping
                if (0.6*base_overlapping*hight_overlapping) == (0.5*tops[tri][1]*tops[tri][1]*2):
                    break

    return all_area
mountain_scape([[1,3],[5,3],[5,5],[8,4]])