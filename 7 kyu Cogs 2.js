/*
Kata Task
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
For C and NASM coders, the returned array will be free'd.
*/

function cogRpm(cogs, n) {
    let result = [0, 0];
    
    if (cogs.length === 0) {
        return result;
    }
    
    else if (cogs.length === 1) {
        result[0] = 1;
        result[1] = 1;
        return result;
    }
    
    else {
        let Rn, first, last;
        
        if (n === 0) {
            Rn = cogs[0] / cogs[cogs.length - 1];
            if (cogs.length % 2 !== 0) {
                result[0] = 1;
                result[1] = Rn;
            }
            else {
                result[0] = 1;
                result[1] = -Rn;
            }
        }
        
        else if (cogs.length === n + 1) {
            Rn = cogs[n] / cogs[0];
            if (cogs.length % 2 === 0) {
                result[0] = -Rn;
                result[1] = 1;
            }
            else {
                result[0] = Rn;
                result[1] = 1;
            }
        }
        
        else {
            let right_side = cogs.slice(n);
            let Rn_r = right_side[0] / cogs[cogs.length - 1];
            if (right_side.length % 2 !== 0) {
                last = Rn_r;
            }
            else {
                last = -Rn_r;
            }
            
            let left_side = cogs.slice(0, n + 1);
            let Rn_l = -(cogs[n] / cogs[0]);
            if (left_side.length % 2 !== 0) {
                first = -Rn_l;
            }
            else {
                first = Rn_l;
            }
            
            result[0] = first;
            result[1] = last;
        }
    }
    
    return result;
}
