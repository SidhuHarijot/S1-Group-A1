"""Question number 1:"""
#boolean variable to check for the eligibility of given number.
eligible = False
#Initializing variable outside of loop
N = 0
while eligible == False:
    N = int(input("Enter any number greater than 1: "))
    #Check if input is eligible
    if N > 1:
        # Number is eligible break the loop
        eligible = True
    else:
        # Number not eligible display error message and try again.
        print("Number is not greater than 1. Please try again.")
# Initializing variable outside of loop
sum = 0
for n in range(N + 1):
    # Adding n to sum, n starts from 0, 1 ,2, 3, ....N. it is not modified to make it start from 0 since it doesn't effect the outcome
    sum += n
#Print the result.
print("The average comes out to be {}".format(sum/N))
