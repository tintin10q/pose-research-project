actions = "ShoulderLeft, ElbowLeft, WristLeft, ShoulderRight, ElbowRight, WristRight, ThumbLeft, ThumbRight".split(", ")

actions_final = ""
for s in range(2):
    for action in actions:
        actions_final += f"S{s}{action}3Dx,"
        actions_final += f"S{s}{action}3Dy,"
        actions_final += f"S{s}{action}3Dz,"
        actions_final += f"S{s}{action}2Dx,"
        actions_final += f"S{s}{action}2Dz,"
    else:
        actions_final += f"S{s}ActionName,"

print(actions_final)