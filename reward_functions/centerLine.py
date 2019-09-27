def reward_function(params):
    max_reward = 10
    min_reward = 1
    reward = 0

    max_speed = 5
    min_speed = 0.25

    marker_1 = 0.1 * params['track_width']
    marker_2 = 0.2 * params['track_width']
    marker_3 = 0.3 * params['track_width']
    marker_4 = 0.4 * params['track_width']
    marker_5 = 0.5 * params['track_width']

    steering = abs(params['steering_angle']) # Only need the absolute steering angle

    if params['distance_from_center'] <= marker_1:
        reward += max_reward
    elif params['distance_from_center'] <= marker_2:
        reward += (max_reward-(1*min_reward)) #9 
    elif params['distance_from_center'] <= marker_3:
        reward += (max_reward-(5*min_reward)) #5
    elif params['distance_from_center'] <= marker_4:
        reward += (max_reward-(9*min_reward)) #1
    elif params['distance_from_center'] <= marker_5:
        reward = 1e-3                   #0.003

    if (params['all_wheels_on_track']):
        reward *= max_reward
    else:
        reward /= max_reward

# maximum punishment if not in route
    if(params['is_reversed']):
        reward = 1e-3

    # checking its in corner and speed is maximum so it should be maximum minus reward
    if params['distance_from_center'] <= marker_5:
        if abs(params['speed']) > 0.8:
            reward = 1e-3
    
    # if he is in center line then speed max
    if params['distance_from_center'] <= marker_1 or params['distance_from_center'] <= marker_2 :
        if abs(params['speed']) >2 :
            reward *= max_reward

    # pennelize steering

    # Penalize reward if the agent is steering too much

    ABS_STEERING_THRESHOLD = 15    
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    
    




    return float(reward)
