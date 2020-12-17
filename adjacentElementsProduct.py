# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

# 7 and 3 produce the largest product.
def adjacentElementsProduct(inputArray):
    # Make an empty array
    finalArray = []
    # Iterate over the list and append the products and then find largest product
    for i in range(len(inputArray) - 1):
        # Append product of inputArray to final array
        # Multiply i  
        finalArray.append(inputArray[i]*inputArray[i+1])
    # Want to know the greatest
    result = max(finalArray)
    return result   