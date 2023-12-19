import numpy

"""
    example of uses of numpy in data analysis
    given the data below one could perform 2 operations that may solve the problem:

    harder/long-way: creating variables and finding the solution
    simpler-way: use of the zip() method to solve the problem

    REGION      TEMP        RAINFALL        HUMIDITY
    Kanto       73          61              43
    Johto       91          88              64
    Hoenn       87          134             58
    Sinnon      102         43              37
    Unora       69          96              70

    w1,w2,w3 = 0.3, 0.2, 0.5
"""

##harder/long-way

w1,w2,w3 = 0.3, 0.2, 0.5
Kanto_temp = 73
Kanto_Humid = 43
Kanto_Rainfall = 61

kanto_crop_Yield = Kanto_temp *w1 + Kanto_Humid * w3 + Kanto_Rainfall * w2
print("The crop yield of Kanto region is {}".format(kanto_crop_Yield))

##using zip() from numpy

weights = 0.3, 0.2, 0.5
kanto_Region = [73, 61, 43]
Johto_Region = [91, 88, 64]
Hoenn_Region = [87, 134, 58]
Sinnon_Region = [102, 45, 37]
Unona_Region = [69, 96, 70]

def cropYield(region, weight):
    result = 0
    for x,z in zip(region, weight):
        result += x * z

    return result

cropYield = cropYield(kanto_Region, weights)    
print("\n\n")
print("The crop yield of Kanto Region is {}".format(cropYield))
