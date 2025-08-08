floats = [
    0.08609706163406, 0.08145088702440, 0.06972485780716, 0.07918803393841,
    0.08136864006519, 0.08513513952494, 0.08950218558311, 0.08868616074324,
    0.10219442844391, 0.09897862374783, 0.06762805581093, 0.09653261303902,
    0.09639212489128, 0.08932472020388, 0.08893045783043, 0.10165258497000,
    0.09411338716745, 0.09809825569391, 0.11859381198883, 0.11554650962353,
    0.08864139765501, 0.09305465966463, 0.09771092981100, 0.09979016333818,
    0.09484998136759, 0.09490405023098, 0.08948394656181, 0.08469844609499
]

# Create list with tuples containing skin serial number and float value
skin_data = [(i + 1, float_val) for i, float_val in enumerate(floats)]

# Sort skin_data based on the float value (ascending order)
sorted_skin_data = sorted(skin_data, key=lambda x: x[1])

target_avg_float = 0.0908  # Desired average float for each tradeup
group_size = 10  # Number of skins per tradeup

group1 = []
group2 = []
assigned_skins = 0  # Track total skins assigned to both tradeups

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
    elif len(group2) < group_size and (not group1 or sum(fval for _, fval in group1) / len(group1) <= target_avg_float):
        group2.append((serial_num, float_val))
        assigned_skins += 1

# Calculate average float for each group (handle empty groups)
avg_float1 = sum(float_val for _, fval in group1) / len(group1) if group1 else 0
avg_float2 = sum(float_val for _, fval in group2) / len(group2) if group2 else 0

print("Tradeup 1:")
for serial_num, float_val in group1:
    print(f"  Serial Number: {serial_num}, Float Value: {float_val}")
print(f"  Average Float: {avg_float1:.4f}")

print("\nTradeup 2:")
if group2:
    for serial_num, float_val in group2:
        print(f"  Serial Number: {serial_num}, Float Value: {float_val}")
    print(f"  Average Float: {avg_float2:.4f}")
else:
    print("  No skins assigned to Tradeup 2.")

    