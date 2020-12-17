# After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).
def matrixElementsSum(matrix):
    if len(matrix) > 1:
        for row in range(1, len(matrix)):
            for room in range(len(matrix[row])):
                if matrix[row - 1][room] == 0:
                    matrix[row][room] = 0
    sum = 0
    for row in matrix:
        for room in row:
            sum += room
    return sum