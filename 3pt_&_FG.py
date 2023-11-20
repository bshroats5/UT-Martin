import matplotlib.pyplot as plt
# Data for Eastern Kentucky
eastern_kentucky_fg = 29
eastern_kentucky_fga = 79
eastern_kentucky_3pt = 9
eastern_kentucky_3pta = 32
# Data for UT-M
utm_fg = 34
utm_fga = 74
utm_3pt = 11
utm_3pta = 26
# Calculate percentages
eastern_kentucky_fg_percentage = eastern_kentucky_fg / eastern_kentucky_fga * 100
eastern_kentucky_3pt_percentage = eastern_kentucky_3pt / eastern_kentucky_3pta * 100
utm_fg_percentage = utm_fg / utm_fga * 100
utm_3pt_percentage = utm_3pt / utm_3pta * 100
# Create the graph
fig, ax = plt.subplots()
# Set the labels
ax.set_xlabel("Team")
ax.set_ylabel("Percentage")
ax.set_title("Field Goal and 3-Point Percentages")
# Set the bars
ax.bar(["Eastern Kentucky", "UT-Martin"], [eastern_kentucky_fg_percentage, utm_fg_percentage], label="Field Goal Percentage")
ax.bar(["Eastern Kentucky", "UT-Martin"], [eastern_kentucky_3pt_percentage, utm_3pt_percentage], label="3-Point Percentage")
# Set the colors
eastern_kentucky_color = "#800000"  # Maroon
eastern_kentucky_3pt_color = "#000000"  # Black
utm_color = "#FFA500"  # Orange
utm_3pt_color = "#000080"  # Navy Blue
# Set the bars with custom colors
ax.bar(["Eastern Kentucky", "UT-Martin"], [eastern_kentucky_fg_percentage, utm_fg_percentage], label="Field Goal Percentage", color=[eastern_kentucky_color, utm_color])
ax.bar(["Eastern Kentucky", "UT-Martin"], [eastern_kentucky_3pt_percentage, utm_3pt_percentage], label="3-Point Percentage", color=[eastern_kentucky_3pt_color, utm_3pt_color])

# Add a legend
ax.legend()
ax.legend(loc='center right', bbox_to_anchor=(1.13, 0.5))

# Show the graph
plt.show()