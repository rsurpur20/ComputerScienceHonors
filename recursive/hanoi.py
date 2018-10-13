
n=int(input("Number of discs?"))
left=True #if this was false, then all the discs would not end up on the right most pole

def moves(n, left):
    print(left)
    if n==0: #if there are no discs
        return
    moves(n-1,not left) #call the function to make sure there isn't 1 disc

    if  left:
        # print(left)
        print(str(n)+'  left')
    else:
        print(str(n)+'  right')
        moves(n-1,not left)

moves(n,not left)
