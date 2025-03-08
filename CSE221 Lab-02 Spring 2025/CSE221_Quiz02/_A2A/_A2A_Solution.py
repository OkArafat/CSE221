def solve(N, S, A):
    I, J = 0, 0
    # Place your code here
    ok=0
    ok_1=N-1
    addtion=0
    while ok<ok_1:
        addtion=A[ok]+A[ok_1]
        if S==addtion:
            I=ok+1
            J=ok_1+1
            return(I,J)
        elif addtion<S :
            ok=ok+1
        elif addtion > S:
            ok_1=ok_1-1
    I=-1
    J=-1
        
    return (I, J)
