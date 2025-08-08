def swap_skins(group1, group2, target_avg):
  """
  Swaps skins between groups to achieve closer average float to target.

  Args:
      group1: List of tuples (serial_num, float_value) for Tradeup 1.
      group2: List of tuples (serial_num, float_value) for Tradeup 2.
      target_avg: Desired average float for both tradeups.

  Returns:
      A tuple containing the updated groups (group1, group2).
  """

  # Loop until stopping criteria is met (replace with your conditions)
  while True:
    # Identify swap candidates
    swap_candidates_t1 = [
        (serial_num, float_val) for serial_num, float_val in group1 if float_val >= target_avg
    ]
    swap_candidates_t2 = [
        (serial_num, float_val) for serial_num, float_val in group2 if float_val < target_avg
    ]

    # Check if there are any swap candidates
    if not swap_candidates_t1 or not swap_candidates_t2:
      break

    # Select swap candidates (prioritize larger impact)
    candidate_t1 = max(swap_candidates_t1, key=lambda x: x[1])
    candidate_t2 = min(swap_candidates_t2, key=lambda x: x[1])

    # Remove candidates from their respective groups
    group1 = [x for x in group1 if x != candidate_t1]
    group2 = [x for x in group2 if x != candidate_t2]

    # Add swapped candidates to the other group
    group1.append(candidate_t2)
    group2.append(candidate_t1)

    # Recalculate average floats
    avg_float1 = sum(fval for _, fval in group1) / len(group1) if group1 else 0
    avg_float2 = sum(fval for _, fval in group2) / len(group2) if group2 else 0

    # Check if target averages are achieved (replace with your tolerance)
    if abs(avg_float1 - target_avg) <= 0.001 and abs(avg_float2 - target_avg) <= 0.001:
      break

  return group1, group2

def group_and_swap_skins(floats, target_avg, group_size):
  """
  Groups skins into two tradeups and performs swapping to achieve closer average float to target.

  Args:
      floats: List of float values for each skin.
      target_avg: Desired average float for both tradeups.
      group_size: Number of skins per tradeup.

  Returns:
      A tuple containing the updated groups (group1, group2).
  """

  # Create list with tuples containing skin serial number and float value
  skin_data = [(i + 1, float_val) for i, float_val in enumerate(floats)]

  # Sort skin_data based on the float value (ascending order)
  sorted_skin_data = sorted(skin_data, key=lambda x: x[1])

  group1 = []
  group2 = []
  assigned_skins = 0

  # Iterate through sorted skin data (avoiding zero float values)
  for serial_num, float_val in (x for x in sorted_skin_data if x[1] > 0):

    # Check if both groups are already full or exceeding target average
    if assigned_skins >= 2 * group_size:
      break

    # Now check which group needs a skin (considering average)
    # Prioritize adding to Tradeup 1 if possible
    if len(group1) < group_size:
      group1.append((serial_num, float_val))
      assigned_skins += 1
    elif len(group2) < group_size and (not group1 or sum(fval for _, fval in group1) / len(group1) <= target_avg):
      group2.append((serial_num, float_val))
      assigned_skins
