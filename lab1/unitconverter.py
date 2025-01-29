def main():
    measure=input("Enter a distance or weight: ")
    new_measure=measure.split()
    num=float(new_measure[0])
    unit=new_measure[1]
    in_cm_ratio=1/2.54
    m_yd_ratio=1/0.9144
    oz_gm_ratio=1/28.349523125
    kg_lb_ratio=1/0.45359237
    if unit=="in":
        cm_measure=format(num/in_cm_ratio,".2f")
        print(f"{measure} = {cm_measure} cm")
    elif unit=="cm":
        in_measure=format(num*in_cm_ratio,".2f")
        print(f"{measure} = {in_measure} in")
    elif unit=="yd":
        meter_measure=format(num/m_yd_ratio,".2f")
        print(f"{measure} = {meter_measure} m")
    elif unit=="m":
        yd_measure=format(num*m_yd_ratio,".2f")
        print(f"{measure} = {yd_measure} yd")
    elif unit=="oz":
        gm_measure=format(num/oz_gm_ratio,".2f")
        print(f"{measure} = {gm_measure} gm")
    elif unit=="gm":
        oz_measure=format(num*oz_gm_ratio,".2f")
        print(f"{measure} = {oz_measure} oz")
    elif unit=="lb":
        kg_measure=format(num/kg_lb_ratio,".2f")
        print(f"{measure} = {kg_measure} kg")
    elif unit=="kg":
        lb_measure=format(num*kg_lb_ratio,".2f")
        print(f"{measure} = {lb_measure} lb")
    else:
        print("Invalid input.")
main()
