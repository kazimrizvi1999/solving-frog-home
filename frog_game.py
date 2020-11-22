# Recursive Solution for the Frog Hopping Puzzle/Game

#this function resturns a boolean, telling whether a frog at
# index = frogindex can move or is stuck
def frogcanmove(frogindex, lst):
    if lst[frogindex] == "":
        return False
    if lst[frogindex] == "LtR":
        if frogindex == len(lst)-1:
            return False
        if frogindex == len(lst)-2:
            if lst[frogindex+1] != "": 
                 return False
            return True
        if lst[frogindex+1] == "":
            return True
        if lst[frogindex +1] != "":
            if lst[frogindex+2] == "":
                return True
            return False
    else:
        if frogindex == 0:
            return False
        if frogindex == 1:
            if lst[0] != "":
                return False
            return True
        if lst[frogindex-1] == "":
            return True
        if lst[frogindex-1] != "":
            if lst[frogindex-2] == "":
                return True
            return False
        
#the func below prints all possible steps that you need to follow to win a game
#lst = initial state of game, path is what it prints if it was able to reach
# the goal, count is for printing steps for user's ease
#initial state can be kept arbitrary + you can also add as many frogs as you want
        
def tellpath(lst, path = "", count = 1):
    originallst = lst 
    originalpath = path 
    ocount = count + 0
    if lst == ["RtL", "RtL", "RtL", "", "LtR", "LtR", "LtR"]:
        print(path+"\n")
        return
    #move whichever frog can move and call recursively
    for frogindex in range(0, len(lst)):
        lst = originallst + []
        path = originalpath + ""
        count = ocount + 0
        if frogcanmove(frogindex, lst):
            if lst[frogindex] == "LtR":
                if lst[frogindex+1] == "":
                    lst[frogindex+1] = lst[frogindex]
                    lst[frogindex] = ""
                    toindex = frogindex+1
                else:
                    lst[frogindex+2] = lst[frogindex]
                    lst[frogindex] = ""
                    toindex = frogindex+2
            else:
                if lst[frogindex-1] == "":
                    lst[frogindex-1] = lst[frogindex]
                    lst[frogindex] = ""
                    toindex = frogindex-1
                else:
                    lst[frogindex-2] = lst[frogindex]
                    lst[frogindex] = ""
                    toindex = frogindex-2
            path += str(count) + ". Move frog at index " + str(frogindex) + " to the index " + str(toindex) + ".\n" + str(lst) + "\n"
            tellpath(lst, path, count+1) 
            
    return

print("Note: 'LtR' = frog that's supposed to move Left to Right, 'RtL' = frog that is supposed to move Right to Left \n")
print("Initial state = ['LtR', 'LtR', 'LtR', '', 'RtL', 'RtL', 'RtL']" + "\n")
tellpath(["LtR", "LtR", "LtR", "", "RtL", "RtL", "RtL"])

#it can be inferred that solutions for this problem are symmetrical
#i.e. vice versa of each other
