#W1D1 SE116 Review Demo - split into prts in Canvas

#Braedin Yarletts
#Lab #1 
#July 17th 

#PROGRAM PROMPT: This is tempF to tempC cnversion program that averages all temps entered

#VARIBLE DICTIONARY

#---------FUNCTIONS---------------------------------------------------------------------------------------
def converter(f):

    '''this function is passed a temp F value, convert to C, nd returns said value'''

    c = (f - 32) * (5 / 9)

    return c #literallly returns to the pointof functon call








#---------MAIN CORE---------------------------------------------------------------------------------------

#initilizing known or needed values
tempCount = 0
tempSum  = 0

answer = "y"
degree = u'\N{DEGREE SIGN}'

while answer.lower() == "y" or answer.lower() == "yes":

    tempF = float(input("\n\t\tEnter temperature in Fahrenheit" ))

    tempCount += 1   #tempCount = tempCount + 1
    tempSum += tempF

    #convert F to C 


    tempC = converter(tempF)

    print (f"\t\tTemperature: {tempF:.1f}{degree}F  |  {tempC:.1f}{degree}C")




    answer = input("Would you like to enter nother temp? [y/n]: ")

    #error trap
    while answer.lower() != "y" and answer != "no":
        print("\t\t***INVALID ENTRY***")
        answer = input("Would you like to enter nother temp? [y/n]: ")


if tempCount != 0:
    avgTemp = tempSum / tempCount
    avgC = converter(avgTemp)
    
    print(f"\n\nYou have entered {tempCount} temperatures for an average of {avgTemp:.2f}F  |  {avgC:.1}{degree}C")
    print("\n\nThank you. Goodbye.\n\n")

else:
    print("You did not enter ny temperature:")
print("\n\nThank you. Goodbye.\n\n")

