
seq1 = "AAAAATC"
seq2 = "AAACGGG"
gap = -2
match = 1
mismatch = 0


def get_align(seq1,seq2, gap = -2, match = 1, mismatch = 0):
    length1 = len(seq1)
    length2 = len(seq2)

    matrix = [[0]*(length1 + 1) for x in range(length2 + 1)]

    for i in range(length1 + 1):
        matrix[0][i] = gap*i

    #creating the gap penalty for the column
    for j in range(length2 + 1):
        matrix[j][0] = gap*j
    for i in range(1, len(matrix)): # i for seq2 the row, j for seq1 the column
        for j in range(1, len(matrix[0])):
            upper = matrix[i-1][j] + matrix[0][j]
            left = matrix[i][j-1] + matrix[i][0]
            if seq1[j-1] == seq2[i-1]:
                diag = matrix[i-1][j-1] + match
            else:
                diag = matrix[i-1][j-1] + mismatch
        
            matrix[i][j] = max(upper, left, diag)
    seq1_mod = "*" + seq1
    seq2_mod = "*" + seq2

    align1 = ""
    align2 = ""

    i = length2 
    j = length1 
    while i > 0 and j > 0:
        if seq1_mod[j] == seq2_mod[i] or max(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) == matrix[i-1][j-1]:
            align1 += seq1_mod[j]
            align2 += seq2_mod[i]
            i -= 1
            j -= 1
        elif max(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) == matrix[i][j-1]: #to the left
            align1 += seq1_mod[j]
            align2 += "-"
            j -= 1
        elif max(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) == matrix[i-1][j]:
            align1 += "-"
            align2 += seq2_mod[i]
            i -= 1

    return(align1[::-1] + "\n"+ align2[::-1] +"\n" + "sequencing score: " + str(matrix[length2][length1]))


