            
def get_robo_dict():
    robo_dict = dict()
    standard = [1, 4, 5]
    hero = 2
    engineer = 3
    
    for i in range(1, 6):
        if i in standard:
            robo_dict["red " + str(i)] = 1000
            robo_dict["blue " + str(i)] = 1000
        elif i == hero:
            robo_dict["red " + str(i)] = 2000
            robo_dict["blue " + str(i)] = 2000            
        
        elif i == engineer:
            robo_dict["red " + str(i)] = 5000
            robo_dict["blue " + str(i)] = 5000
    
    robo_dict["red base"] = 10000
    robo_dict["blue base"] = 10000    
    
    robo_dict["17mm"] = 50
    robo_dict["42mm"] = 500
    
    robo_dict["red_safe"] = True
    robo_dict["blue_safe"] = True
    
    robo_dict["red_damage"] = 0
    robo_dict["blue_damage"] = 0
    
    return robo_dict


    
def roboMaster(shots):
    robo_dict = get_robo_dict()
    
    for shot in shots:
        team = shot[1].split()[0]
        
        if shot[1] == team + " base":
            if not robo_dict[team + "_safe"]:
                robo_dict[shot[1]] -= robo_dict[shot[2]]
            continue
            
        robo_dict[shot[1]] -= robo_dict[shot[2]]
        robo_dict[team + "_damage"] += robo_dict[shot[2]]
        
        if robo_dict[shot[1]] <= 0:
            robo_dict[team + "_safe"] = False
    
    if robo_dict["red base"] > robo_dict["blue base"]:
        return "red"
    elif robo_dict["blue base"] > robo_dict["red base"]:
        return "blue"
    else:
        if robo_dict["red_damage"] < robo_dict["blue_damage"]:
            return "red"
        elif robo_dict["blue_damage"] < robo_dict["red_damage"]:
            return "blue"
        else:
            return  "draw"
        