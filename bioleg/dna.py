def secuerepe(seq1, seq2):
    i1 = 0

    result = ''
    repe = ''

    while i1 < len(seq1):
        i2 = 0
        while i2 < len(seq2) and i1 < len(seq1):
            # print(seq1, seq2)
            # print(' '*i1+'^'+' '*(len(seq1)-i1-1), ' '*i2+'^'+' '*(len(seq2)-i2-1))
            if seq1[i1] == seq2[i2]:
                if repe == '':
                    first1 = i1
                repe += seq1[i1]
                i1 += 1
            else:
                if len(repe) > len(result):
                    result = repe
                if len(repe)>0:
                    i1 = first1
                repe = ''
            i2 += 1
            # print('/{}/'.format(repe))
        if len(repe) > len(result):
            result = repe
        i1 = first1+1
        repe = ''

    return result

