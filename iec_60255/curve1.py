def IEC_255_Trip_Time (pickup, curve, TMS, fault_current, debug = False):
    # Given IEC 255 curve parameters and a fault current, returns the tripping time in seconds.
    # pickup in amps
    # curve type: "SI", "VI", or "EI"
    # tms is time dial, a positive nonzero number
    # current is in amps
    # This function assumes the curve goes definite time after 20x setting.

    # IEC 60255 curve constants
    K = {"SI":0.14, "VI": 13.5, "EI": 80.0}[curve]
    alpha = {"SI":0.02, "VI": 1.00, "EI": 2.00}[curve]
    
    I_per_unit = fault_current / pickup

    if I_per_unit > 20.0:
        I_per_unit = 20.0 # IEC curves usually go definite time at 20x setting

    t = K * TMS / ( I_per_unit ** alpha - 1 )
    
    return t

def IEC_255_TMS_Calc (pickup, curve, target_current, target_time, debug = False):

    I_per_unit = target_current / pickup
    if I_per_unit > 20.0:
        I_per_unit = 20.0 # IEC curves usually go definite time at 20x setting

    # IEC 60255 curve constants
    K = {"SI":0.14, "VI": 13.5, "EI": 80.0}[curve]
    alpha = {"SI":0.02, "VI": 1.00, "EI": 2.00}[curve]

    TMS = target_time / K * ( I_per_unit ** alpha - 1 )
    
    return TMS
    

    
