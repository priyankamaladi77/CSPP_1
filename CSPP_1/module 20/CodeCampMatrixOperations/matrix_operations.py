'''matrix operations'''
import copy
def mult_matrix(mat1, mat2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    res = copy.deepcopy(mat1)
    for i in range(0, len(mat1), 1):
        for j in range(0, len(mat2[0]), 1):
            res[i][j] = 0
            for k in range(0, len(mat2), 1):
                res[i][j] = int(res[i][j])
                res[i][j] = int(mat1[i][k])*int(mat2[k][j])
    return res

def add_matrix(mat1, mat2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    res = copy.deepcopy(mat1)
    if len(mat1) == len(mat2):
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                temp = int(res[i][j])
                temp += int(mat2[i][j])
                res[i][j] = temp
        return res
    else:
        print("Error: Matrix shapes invalid for addition")
        return None


def read_matrix(size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    ro1 = int(size[0])
    col1 = int(size[1])
    count = 0
    matrix = []
    for _ in range(0, ro1, 1):
        row = input().split()
        matrix.append(row)
        count += len(row)
    # if size[0] != len(matrix):
    #     print("Error: Invalid input for the matrix")
    #     return None
    # for index in matrix:
    #     if len(matrix) != size[1]:
    #         print("Error: Invalid input for the matrix")
    #         return None

    if count != ro1*col1:
        print("Error: Invalid input for the matrix")
        return None
    else:
        return matrix

def main():
    ''' to read the functions'''
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    matrix1 = input().split(',')
    mat1 = read_matrix(matrix1)
    matrix2 = input().split(',')
    mat2 = read_matrix(matrix2)
    if mat1 ==  None or mat2 ==  None:
        return None
    print(add_matrix(mat1, mat2))
    print(mult_matrix(mat1, mat2))

if __name__ == '__main__':
    main()
