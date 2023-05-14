def IEC_255_Trip_Time (pickup, curve, TMS, fault_current, debug = False):
    # Given IEC 255 curve parameters and a fault current, returns the tripping time.
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

    if debug:
        print ("Trip time: %.3f sec | Pickup %.2f A, curve %s, TMS %.2f xt, fault current %.2f A (%.2f x setting)" % 
            t,
            pickup,
            curve,
            TMS,
            fault_current,
            I_per_unit,
        )
    return t

def IEC_255_TMS_Calc (pickup, curve, target_current, target_time, debug = False):

    I_per_unit = target_current / pickup
    if I_per_unit > 20.0:
        I_per_unit = 20.0 # IEC curves usually go definite time at 20x setting

    # IEC 60255 curve constants
    K = {"SI":0.14, "VI": 13.5, "EI": 80.0}[curve]
    alpha = {"SI":0.02, "VI": 1.00, "EI": 2.00}[curve]

    TMS = target_time / K * ( I_per_unit ** alpha - 1 )

    if debug:
        print "TMS calc: %.2f xt | Pickup %.2f A, curve %s, target current %.2f A (%.2f x setting), target time %.2f sec" % (
            TMS,
            pickup,
            curve,
            target_current,
            I_per_unit,
            target_time,
        )

    return TMS
