def longest_slide_down(pyramid):
    result = pyramid[0][0]
    beforeIndex = 0
    for pyr in pyramid[1:]:
        result += max(pyr[beforeIndex:beforeIndex+2])
        beforeIndex = pyr.index(max(pyr[beforeIndex:beforeIndex+2]))
    return result

##TODO: create an algorithm that checks if we choose diffrent num in earlier step of pyramid we can now have bigger sum

print(longest_slide_down([
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ]))





#        0
#       234
#      23456
#     2344567
#    234567889
#   34556778899
#  2345677899898
# 256778899000098
#23445444444444444