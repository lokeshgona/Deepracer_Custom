def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    import math
    # Read input parameters
    #distance_from_center = params['distance_from_center']
    #track_width = params['track_width']
    #steering = (params['steering_angle']) # Only need the absolute steering angle
    step_speed = params['step_speed']
    #closest_waypoints = params['closest_waypoints']
    #waypoints = params['waypoints']
    step_dis = params['step_dis']
    #heading = params['heading']
    #is_left_of_center = params['is_left_of_center']

    reward = 1e-3
    

    '''def angle_cal(next_point, prev_point):
        if next_point > len(waypoints)-1:
            next_point -= (len(waypoints)-1)
        if prev_point > len(waypoints)-1:
            prev_point -= (len(waypoints)-1)
        next_point = waypoints[next_point]
        prev_point = waypoints[prev_point]
        track_dir= math.degrees(math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]))
        return(track_dir)

    track_angle1 = abs(angle_cal(closest_waypoints[1]+1, closest_waypoints[1]) - angle_cal(closest_waypoints[1], closest_waypoints[0]))
    track_angle2 = abs(angle_cal(closest_waypoints[1]+3, closest_waypoints[1]+2) - angle_cal(closest_waypoints[1]+2, closest_waypoints[1]+1))
    track_angle3 = abs(angle_cal(closest_waypoints[1]+5, closest_waypoints[1]+4) - angle_cal(closest_waypoints[1]+4, closest_waypoints[1]+3))
    track_angle4 = abs(angle_cal(closest_waypoints[1]+7, closest_waypoints[1]+6) - angle_cal(closest_waypoints[1]+6, closest_waypoints[1]+5))

    if 320 < track_angle1 < 420:
        track_angle1 = abs(360-track_angle1)
    if 320 < track_angle2 < 420:
        track_angle2 = abs(360-track_angle2)
    if 320 < track_angle3 < 420:
        track_angle3 = abs(360-track_angle3)
    if 320 < track_angle4 < 420:
        track_angle4 = abs(360-track_angle4)
    if 150 < track_angle1 < 320:
        track_angle1 = abs(180-track_angle1)
    if 150 < track_angle2 < 320:
        track_angle2 = abs(180-track_angle2)
    if 150 < track_angle3 < 320:
        track_angle3 = abs(180-track_angle3)
    if 150 < track_angle4 < 320:
        track_angle4 = abs(180-track_angle4)

    #normalized average track curve
    avg_track_angle = (track_angle1+track_angle2+track_angle3+track_angle4)/95

    #angle_dif = abs(angle_two - heading)'''

    reward = step_speed*step_dis


    '''min_speed = 3.3 * (1-avg_track_angle)

    if avg_speed >= min_speed:
        reward = 1
    else:
        if abs(avg_speed - min_speed) <= 1:
            reward = (1- abs(avg_speed - min_speed))**2'''

    return float(reward)
