def largest_histogram(histogram):
    all_rect = [];

    if len(histogram) == 1:
        return histogram[0]
    for i in range(len(histogram)):
        for y in range (histogram[i],0,-1):
            count_rect = 1
            for k in range(i+1,len(histogram)):
                # print ( y , histogram[k])
                if y<=histogram[k]:
                    count_rect+=1
                    if k == len(histogram)-1:
                        all_rect.append(y*count_rect)
                else:
                    all_rect.append(y*count_rect)
                    break
    return max(all_rect)


# def largest_histogram(histogram):
#     all_rect = [];
#     if len(histogram) == 1:
#         return histogram[0]
#     maxx = max(histogram);
#     count_max=histogram.count(maxx)
#     index_max = histogram.index(maxx)
#     print(index_max)

#     # for i in range(maxx) :
#     #     for k in range(2):
#     #         for
#     return all_rect

#largest_histogram([0,3,6,9,12,15,18,22,25,28,31,34,37,41,44,47,50,53,56,60,63,66,69,72,75,79,82,85,88,91,94,97,101,104,107,110,113,116,119,123,126,129,132,135,138,141,145,148,151,154,157,160,163,166,169,173,176,179,182,185,188,191,194,197,201,204,207,210,213,216,219,222,225,228,231,235,238,241,244,247,250,253,256,259,262,265,268,271,274,277,280,283,286,289,292,296,299,302,305,308,311,314,317,320,323,326,329,332,335,338,340,343,346,349,352,355,358,361,364,367,370,373,376,379,382,385,388,391,393,396,399,402,405,408,411,414,417,419,422,425,428,431,434,437,439,442,445,448,451,454,456,459,462,465,468,470,473,476,479,482,484,487,490,493,495,498,501,504,506,509,512,514,517,520,523,525,528,531,533,536,539,541,544,547,549,552,555,557,560,562,565,568,570,573,575,578,581,583,586,588,591,593,596,598,601,603,606,609,611,614,616,618,621,623,626,628,631,633,636,638,641,643,645,648,650,653,655,657,660,662,665,667,669,672,674,676,679,681,683,686,688,690,692,695,697,699,701,704,706,708,710,713,715,717,719,721,724,726,728,730,732,734,737,739,741,743,745,747,749,751,753,756,758,760,762,764,766,768,770,772,774,776,778,780,782,784,786,788,790,792,794,795,797,799,801,803,805,807,809,810,812,814,816,818,820,821,823,825,827,829,830,832,834,836,837,839,841,842,844,846,848,849,851,853,854,856,857,859,861,862,864,865,867,869,870,872,873,875,876,878,879,881,882,884,885,887,888,890,891,893,894,895,897,898,900,901,902,904,905,906,908,909,910,912,913,914,915,917,918,919,920,922,923,924,925,926,928,929,930,931,932,933,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,961,962,963,964,965,966,966,967,968,969,970,970,971,972,973,973,974,975,975,976,977,977,978,979,979,980,981,981,982,982,983,984,984,985,985,986,986,987,987,988,988,989,989,990,990,990,991,991,992,992,992,993,993,994,994,994,995,995,995,995,996,996,996,996,997,997,997,997,998,998,998,998,998,998,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,998,998,998,998,998,998,997,997,997,997,997,996,996,996,995,995,995,995,994,994,994,993,993,992,992,992,991,991,991,990,990,989,989,988,988,987,987,986,986,985,985,984,984,983,982,982,981,981,980,979,979,978,977,977,976,975,975,974,973,973,972,971,970,970,969,968,967,967,966,965,964,963,962,961,961,960,959,958,957,956,955,954,953,952,951,950,949,948,947,946,945,944,943,942,941,940,939,938,937,936,935,934,932,931,930,929,928,927,925,924,923,922,921,919,918,917,916,914,913,912,910,909,908,906,905,904,902,901,900,898,897,896,894,893,891,890,888,887,885,884,883,881,880,878,877,875,873,872,870,869,867,866,864,862,861,859,858,856,854,853,851,849,848,846,844,843,841,839,838,836,834,832,831,829,827,825,823,822,820,818,816,814,813,811,809,807,805,803,801,799,798,796,794,792,790,788,786,784,782,780,778,776,774,772,770,768,766,764,762,760,758,756,754,752,750,747,745,743,741,739,737,735,733,730,728,726,724,722,720,717,715,713,711,708,706,704,702,700,697,695,693,690,688,686,684,681,679,677,674,672,670,667,665,662,660,658,655,653,651,648,646,643,641,638,636,634,631,629,626,624,621,619,616,614,611,609,606,604,601,599,596,594,591,589,586,583,581,578,576,573,571,568,565,563,560,557,555,552,550,547,544,542,539,536,534,531,528,526,523,520,517,515,512,509,507,504,501,498,496,493,490,487,485,482,479,476,474,471,468,465,462,460,457,454,451,448,445,443,440,437,434,431,428,426,423,420,417,414,411,408,405,403,400,397,394,391,388,385,382,379,376,373,370,367,365,362,359,356,353,350,347,344,341,338,335,332,329,326,323,320,317,314,311,308,305,302,299,296,293,290,287,284,281,278,275,272,269,266,262,259,256,253,250,247,244,241,238,235,232,229,226,223,220,216,213,210,207,204,201,198,195,192,189,185,182,179,176,173,170,167,164,161,157,154,151,148,145,142,139,136,132,129,126,123,120,117,114,110,107,104,101,98,95,92,88,85,82,79,76,73,69,66,63,60,57,54,50,47,44,41,38,35,32,28,25,22,19,16,13,9,6,3])
largest_histogram([70,60,67,78,89,87,74,40,100,24,66,84,11,99,4,34,21,23,66,34,47,54,51,88,53,7,94,72,28,59,30,44,0,17,96,34,63,6,81,61,26,96,72,5,32,57,1,3,47,13,97,96,9,7,80,5,89,77,7,75,63,59,90,88,16,48,93,33,70,35,57,15,61,81,63,83,33,3,55,63,86,33,94,45,76,99,86,14,96,81,33,32,76,37,56,54,63,11,82,41,90,81,53,42,89,75,98,74,18,73,7,30,10,14,67,59,25,56,41,90,80,17,84,16,45,6,29,87,79,56,33,94,73,72,31,18,30,17,81,64,92,3,94,12,65,23,50,54,52,16,19,39,26,12,75,19,11,69,48,25,64,6,22,19,19,29,41,90,43,41,36,66,91,23,28,4,15,94,89,6,87,4,98,19,12,54,3,66,84,83,28,95,3,55,44,64,86,15,15,37,89,65,100,9,11,6,38,26,62,89,14,29,81,94,47,63,71,56,31,96,68,30,96,77,32,28,82,39,75,67,73,83,70,70,74,50,89,98,27,50,2,42,46,11,59,60,96,90,20,14,92,20,59,8,16,23,69,41,7,64,66,38,30,47,87,82,73,12,82,0,45,100,59,10,42,19,21,22,17,67,33,69,12,100,14,11,20,43,30,20,93,43,14,28,68,55,89,57,48,97,95,88,4,41,61,45,91,0,22,57,40,18,21,97,51,36,67,14,22,6,57,11,31,48,45,83,97,60,14,32,27,65,24,48,94,63,25,50,52,91,55,81,96,33,89,82,21,8,100,93,100,47,18,80,88,81,1,10,81,25,68,95,81,95,53,93,79,23,9,87,63,95,4,68,42,73,16,29,27,44,3,48,90,92,46,66,81,58,98,64,90,95,64,46,73,40,74,67,32,59,61,89,96,42,47,97,70,22,78,70,2,67,39,59,76,78,41,23,84,52,88,89,88,4,17,48,3,41,30,14,30,92,65,87,79,84,21,57,19,62,19,50,13,27,21,83,25,19,72,50,40,12,4,43,60,41,46,45,92,93,16,54,29,38,42,53,93,2,44,98,79,25,34,3,69,74,21,100,92,61,100,22,23,74,70,76,18,10,50,68,96,83,95,69,90,49,61,93,51,55,47,87,53,50,80,31,76,0,64,74,68,11,18,85,99,67,71,88,87,72,10,58,31,82,49,70,10,84,79,23,5,53,25,36,9,33,71,48,4,14,51,71,58,44,17,53,87,62,41,80,90,0,36,48,75,67,28,82,34,75,93,63,66,72,54,41,68,67,82,77,36,74,16,4,96,39,61,64,92,78,86,21,87,43,81,94,76,31,18,50,59,66,57,34,77,27,57,66,65,17,25,90,78,23,52,31,28,71,93,95,62,23,99,48,36,85,22,13,33,13,33,67,63,100,52,94,97,83,45,88,65,9,31,30,97,9,71,45,39,15,39,79,25,62,69,1,30,26,25,74,35,5,22,72,25,3,15,52,94,87,37,46,9,58,90,14,46,39,44,60,53,5,18,12,69,25,55,37,85,3,43,75,20,9,35,1,60,58,83,77,60,75,7,91,76,95,48,91,83,50,3,85,42,31,68,48,94,37,96,89,43,40,24,43,72,8,49,93,26,74,82,63,41,82,74,58,46,39,30,3,58,84,68,84,1,18,26,26,18,40,59,29,22,73,1,74,33,62,73,12,1,43,72,33,44,24,63,18,65,93,18,28,91,87,15,24,84,96,87,6,48,14,99,79,75,25,68,53,26,27,63,74,75,96,94,7,100,91,77,96,32,34,42,19,2,0,68,21,55,21,20,48,84,1,63,96,2,52,53,99,90,82,50,46,23,49,33,26,55,100,37,92,11,70,60,61,30,35,26,10,69,90,54,46,58,96,65,49,8,89,74,52,29,60,93,51,47,27,72,42,12,51,36,34,26,62,13,81,20,97,52,25,44,41,90,18,7,34,99,98,40,49,100,16,84,93,10,35,75,78,96,13,83,38,66,61,26,83,34,13,59,89,22,35,41,45,25,42,69,95,40,43,1,65,44,18,25,81,87,86,43,90,64,16,88,49,6,21,80,89,71,63,25,47,91,93,8,42,61,67,22,67,96,69,45,100,41,48,72,96,3,18,30,37,85,51,84,75,10,99,74,84,91,58,6,8,13,50,94,39,19,73,70,96,0,18,58,29,100,84,92,91,46,48,4,33,60,35,14,45,43,6,42,30,91,0,71,100,55,14,9,99,100,31,83,6,37,48,57])