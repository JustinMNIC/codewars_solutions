"""Kata Task
You are given a list of cogs in a gear train

Each element represents the number of teeth of that cog

e.g. [100, 50, 25] means

1st cog has 100 teeth
2nd cog has 50 teeth
3rd cog has 25 teeth
If the nth cog rotates clockwise at 1 RPM what is the RPM of the cogs at each end of the gear train?

Notes

no two cogs share the same shaft
return an array whose two elements are RPM of the first and last cogs respectively
use negative numbers for anti-clockwise rotation
for convenience n is zero-based
For C and NASM coders, the returned array will be free'd."""


def cog_RPM(cogs, n):
    if len(cogs) == 0:
        return [0, 0]
    elif len(cogs) == 1:
        return [1, 1]
    else:
        if n == 0:
            Rn = cogs[0] / cogs[-1]
            if len(cogs) % 2 != 0:
                return [1, Rn]
            else:
                return [1, -Rn]
            
        elif len(cogs) == n+1:
            Rn = cogs[n] / cogs[0]
            if len(cogs) % 2 == 0:
                return [-Rn, 1]
            else:
                return [Rn, 1]
            
        else:
            first: float
            last: float
            
            right_side = len(cogs[n:])
            Rn_r = cogs[n] / cogs[-1]
            if right_side % 2 != 0:
                last = Rn_r
            else:
                last = -Rn_r
            
            left_side = len(cogs[:n+1])
            Rn_l = -(cogs[n] / cogs[0])
            if left_side % 2 != 0:
                first = -Rn_l
            else:
                first = Rn_l
                
            return [first, last]
        
cogs = [31, 10, 78, 23, 53, 78, 75, 68, 72]
n = 8

print(cog_RPM(cogs, n)) 