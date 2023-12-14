#First we need to use the function in order to calculate the product of a value
#in a list over a period of time.
#Using Def
def calculate_product(myinput_list):
    product = 1
    for usernum in myinput_list:
        product *= usernum
    return product
#Now writing and find the main program.
def main():
  #Now writing the example with the list of numbers.
    myexamplenumber_list =[6,7,8,9]
#Now we have to call  the function and therefore get the result.
    result = calculate_product(myexamplenumber_list)
#Now print the result.
    print("Product of the list values:",result)
#Now run the main function

main()