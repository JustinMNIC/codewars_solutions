"""Kata Task
You are given a list of cogs in a gear train

Each element represents the number of teeth of that cog

e.g. [100, 75] means

1st cog has 100 teeth
2nd cog has 75 teeth
If the first cog rotates clockwise at 1 RPM what is the RPM of the final cog?

(use negative numbers for anti-clockwise rotation)

Notes
no two cogs share the same shaft"""

def cog_RPM(cogs):
    Rn = cogs[0] / cogs[-1]
    if len(cogs) % 2 != 0:
        return Rn
    else:
        return -Rn