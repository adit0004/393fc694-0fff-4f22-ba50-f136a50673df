def cancel(wt,W, originalW = 0):
    if(len(wt) == 0): return [0]
    if(W <= 0): return [0]
    if(originalW == 0):
        originalW = W
    thisW = W
    if(thisW == originalW * 2):
        return "Cannot be cancelled optimally"
    wt.sort()
    solution = []
    for i in range(len(wt) - 1, -1, -1):
        if W >= wt[i]:
            W -= wt[i]
            solution.append(wt[i])
    if(sum(solution) == thisW):
        return solution
    else:
        return cancel(wt, originalW + 1, originalW)
