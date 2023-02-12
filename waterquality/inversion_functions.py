# This module contains the functions that will be used to invert from reflectances to water quality parameters
# The dicionary `functions`` will be used by the waterquality module:
# function = {
#   'name_of_the_parameter': {'function': any_function}, 'units': 'units to be displayed in the report',
#   'name_of_the_parameter2': .....
# }

# Any bands can be used to compute the final value. The name of the band must match the internal name used by WaterDetect
# It is enough to put the band name as an argument in the function

# Below is an example extracted from Nechad et al. (2010)
# def tsm(Red):
#     a = 493.65
#     b = 1.16
#     c = 0.188
#     tsm = (a * Red / (1 - (Red/c)) + b) * -1
    
#     print(Red)
#     return tsm.squeeze()

def tsm(Red):
    a = 610.94
    c = 0.2324
    spm = 610.94 * Red / (1 - (Red/c))
    return spm.squeeze()

functions = {
    'SPM_Nechad': {
        'function': tsm,
        'units': 'mg/l'
    },
}

