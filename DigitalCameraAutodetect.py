# Enter your code here. Read input from STDIN. Print output to STDOUT


#with open("STDIN.txt") as c:
##    contents = c.read()
#c.close()
blue_pixel, green_pixel, red_pixel, = [], [], []
contents = input()
contents = contents.split()
for x in contents:
    x = x.split(",")

    blue_pixel.append(x[0])
    green_pixel.append(x[1])
    red_pixel.append(x[2])
    
totalb = 0
totalg = 0
totalr = 0

for x in blue_pixel:
    totalb = totalb + int(x)    
    
for y in green_pixel:
    totalg = totalg + int(y)   

for z in red_pixel:
    totalr = totalr + int(z)
    
#print (totalb,totalg,totalr)
#print(totalb/len(blue_pixel), totalg/len(green_pixel), totalr/len(red_pixel))

avgb = totalb/len(blue_pixel)
avgg = totalg/len(green_pixel) 
avgr = totalr/len(red_pixel)

if (avgb > 120 ) :
    input("day")
else:
    input("night")
    
