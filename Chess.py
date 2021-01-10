import random
#List of contestants and their experience levels.
Placements =[['X','1'],['G','5'],['V','randint(0,10)']]

#Separating those with high and low experience levels.
Low=[]
High=[]
for i in range(0,len(Placements)):
    if Placements[i][1]<5:
        Low.append(Placements[i])
    else:
        High.append(Placements[i])

#Shuffling after sorting the lists, so they are ordered first.
Low=sorted(Low,key=lambda x: x[0])
High=sorted(High,key=lambda x: x[0])

random.shuffle(Low)
random.shuffle(High)

#Picking the two byes in the first round... one from each list, so it's fair... and then removing them
# for the next shuffle from their current lists.
i = random.randint(0,6)
Lucky=[]
Lucky.append(Low[i])
Lucky.append(High[i])
Low.remove(Low[i])
High.remove(High[i])

print("The left bye goes to",Lucky[0][0],". \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
print("The right bye goes to", Lucky[1][0], ". \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")

#Forming the first-round matchups after another shuffle and pairings. The number comes from the order they
#appear in.
random.shuffle(Low)
random.shuffle(High)
Pairings=[]
Pairings.append(Low[0]+Low[1])
Pairings.append(Low[2]+Low[3])
Pairings.append(Low[4]+Low[5])
Pairings.append(High[0]+High[1])
Pairings.append(High[2]+High[3])
Pairings.append(High[4]+High[5])
print(Pairings)
