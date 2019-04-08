
def triangle_number_list(n):
    sequence=[]
    for i in range(1,n):
        sequence.append( i*(i+1)/2)
    return sequence
