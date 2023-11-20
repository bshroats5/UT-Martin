import matplotlib.pyplot as plt

# Example data for teams
teams = ['UT-Martin Skyhawks', 'Eastern Kentucky Colonels']
fouls = [13, 10]

# Create a bar graph
plt.bar(teams, fouls)

# Define colors for each team
utm_color = 'Navy'
eastern_kentucky_color = 'maroon'

# Create a bar graph with custom colors
plt.bar(teams, fouls, color=[utm_color, eastern_kentucky_color])


# Add title and labels
plt.title('Team Fouls')
plt.xlabel('Teams')
plt.ylabel('Fouls')

# Show the plot
plt.show()
