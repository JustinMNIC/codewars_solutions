"""Karan's company makes software that provides different features based on the version of operating system of the user.

To compare versions, Karan currently parses both version numbers as floats.

While this worked for OS versions 10.6, 10.7, 10.8 and 10.9, the operating system company just released OS version 10.10. This causes his method to fail, as 10.9 is greater than 10.10 when interpreting both as numbers, despite being a lesser version.

Help Karan by writing him a function which compares two versions, and returns whether or not the first one is greater than or equal to the second.

Specification notes:

Versions are provided as strings of one or more integers separated by ..
The version strings will never be empty.
The two versions are not guaranteed to have an equal amount of sub-versions, when this happens assume that all missing sub-versions are zero.
"""

def compare_versions(version1,version2):
    for num in version1.split('.'):
        if num.isdigit() == False:
            return 'Invalid version format'
    for num in version2.split('.'):
        if num.isdigit() == False:
            return 'Invalid version format'
    version1 = version1.split('.')
    version2 = version2.split('.')
    if len(version1) > len(version2):
        version2 += ['0'] * (len(version1) - len(version2))
    elif len(version2) > len(version1):
        version1 += ['0'] * (len(version2) - len(version1))
    for i in range(len(version1)):
        if int(version1[i]) > int(version2[i]):
            return True
        elif int(version1[i]) < int(version2[i]):
            return False
    return True
