def reward_function(params):
  max_reward = 1
  min_reward = 0.1
  reward = 0

  max_speed = 5
  min_speed= 0.25

  marker_1 = 0.1 * params['track_width']
  marker_2 = 0.2 * params['track_width']
  marker_3 = 0.3 * params['track_width']
  marker_4 = 0.4 * params['track_width']
  marker_5 = 0.45 * params['track_width']

  if params['distance_from_center'] <= marker_1:
    reward += 1
  elif params['distance_from_center'] <= marker_2:
    reward += (max_reward-(2*min_reward))
  elif params['distance_from_center'] <= marker_3:
    reward += (max_reward-(4*min_reward))
  elif params['distance_from_center'] <= marker_4:
    reward += (max_reward-(6*min_reward))
  elif params['distance_from_center'] <= marker_5:
    reward += (max_reward-(9*min_reward))
  else:
    reward = 1e-3  
  

  if (params['all_wheels_on_track']):
      reward += max_reward
  else:
      reward -= max_reward

# maximum punishment if not in route
  if(params['is_reversed']):
    reward -= max_reward


  # checking its in corner and speed is maximum so it should be maximum minus reward
  if params['distance_from_center'] <= marker_5 :
    if abs(params['speed']) > 2:
      reward -= max_reward
  


  return float(reward)
