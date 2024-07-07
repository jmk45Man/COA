from subtraction import binary_adder, twos_complement


def restoring_division(Q, M):
    count = len(Q)  
    if len(M) <= count:
        M = M.zfill(count + 1)
    M_comp = twos_complement(M)
   
    A = "0" * len(M)

    for i in range(count):
      
        A = A[1:] + Q[0]
        Q = Q[1:] 
        A = binary_adder(A, M_comp)

        if A[0] == "1":
            
            Q = Q + "0"
            
            A = binary_adder(A, M)
        else:
          
            Q = Q + "1"

    return (Q, A)


if __name__ == "__main__":
    Q = input("Enter dividend: ")
    M = input("Enter divisor: ")
    if int(Q) < int(M):
        quotient, remainder = "0" * len(Q), Q
    else:
        quotient, remainder = restoring_division(Q, M)
    print(f"Quotient = {quotient}, Remainder = {remainder}")

