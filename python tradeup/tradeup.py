import numpy as np

# Given floats
floats = [
    0.08609706163406, 0.08145088702440, 0.06972485780716, 0.07918803393841, 
    0.08136864006519, 0.08513513952494, 0.08950218558311, 0.08868616074324, 
    0.10219442844391, 0.09897862374783, 0.06762805581093, 0.09653261303902, 
    0.09639212489128, 0.08932472020388, 0.08893045783043, 0.10165258497000, 
    0.09411338716745, 0.09809825569391, 0.11859381198883, 0.11554650962353, 
    0.08864139765501, 0.09305465966463, 0.09771092981100, 0.09979016333818, 
    0.09484998136759, 0.09490405023098, 0.08948394656181, 0.08469844609499
]

# Indices to keep track of the original serial numbers
indices = list(range(1, 29))

# Sort floats along with their indices
sorted_floats_indices = sorted(zip(floats, indices))

# Function to find two packs with average float less than 0.0907 but more than 0.0895
def find_packs_within_range(sorted_floats_indices, min_avg, max_avg):
    for i in range(len(sorted_floats_indices) - 9):
        for j in range(i + 10, len(sorted_floats_indices) - 9):
            pack1 = sorted_floats_indices[i:i+10]
            pack2 = sorted_floats_indices[j:j+10]
            avg1 = np.mean([x[0] for x in pack1])
            avg2 = np.mean([x[0] for x in pack2])
            if min_avg < avg1 < max_avg and min_avg < avg2 < max_avg:
                remaining = [x for k, x in enumerate(sorted_floats_indices) if k < i or (k >= i + 10 and k < j) or k >= j + 10]
                return pack1, pack2, remaining
    return None, None, None

# Finding the two packs and the remaining skins within the given range
pack1_within_range, pack2_within_range, remaining_within_range = find_packs_within_range(sorted_floats_indices, 0.077, 0.0908)

pack1_within_range_indices = [x[1] for x in pack1_within_range] if pack1_within_range else []
pack2_within_range_indices = [x[1] for x in pack2_within_range] if pack2_within_range else []
remaining_within_range_indices = [x[1] for x in remaining_within_range] if remaining_within_range else []

# Print descriptive statistics
print("Mean:", np.mean(floats))
print("Standard Deviation:", np.std(floats))

# Assuming mean is around 0.09 and standard deviation is small
min_avg = np.mean(floats) - 0.005  # Adjust based on your analysis
max_avg = np.mean(floats) + 0.005  # Adjust based on your analysis

pack1_within_range, pack2_within_range, remaining_within_range = find_packs_within_range(sorted_floats_indices, min_avg, max_avg)

# Print the results
print("Pack 1 indices:", pack1_within_range_indices)
print("Pack 2 indices:", pack2_within_range_indices)
print("Remaining indices:", remaining_within_range_indices)
