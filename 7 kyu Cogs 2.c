/* Kata Task
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

#include <stdlib.h>

double *cog_rpm(const int cogs[], unsigned count, int n)
{
    double *result = (double *)malloc(2 * sizeof(double));
    
    if (count == 0) {
        result[0] = 0;
        result[1] = 0;
        return result;
    }
    
    else if (count == 1) {
        result[0] = 1;
        result[1] = 1;
        return result;
    }
    
    else {
        double Rn, first, last;
        
        if (n == 0) {
            Rn = (double)cogs[0] / (double)cogs[count - 1];
            if (count % 2 != 0) {
                result[0] = 1;
                result[1] = Rn;
            }
            else {
                result[0] = 1;
                result[1] = -Rn;
            }
        }
        
        else if (count == n + 1) {
            Rn = (double)cogs[n] / (double)cogs[0];
            if (count % 2 == 0) {
                result[0] = -Rn;
                result[1] = 1;
            }
            else {
                result[0] = Rn;
                result[1] = 1;
            }
        }
        
        else {
            int right_side = count - n;
            double Rn_r = (double)cogs[n] / (double)cogs[count - 1];
            if (right_side % 2 != 0) {
                last = Rn_r;
            }
            else {
                last = -Rn_r;
            }
            
            int left_side = n + 1;
            double Rn_l = -(double)(cogs[n]) / (double)(cogs[0]);
            if (left_side % 2 != 0) {
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
