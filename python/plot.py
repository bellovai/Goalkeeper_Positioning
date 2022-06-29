# Import from packages
import matplotlib.pyplot as plt

# Import from files
from data import df_optimal
from config import Config as cfg



# Row
i = 1

# Player location in blue
x_s = df_optimal.at[i, 'x_s']
y_s = df_optimal.at[i, 'y_s']
plt.scatter(x_s, y_s)

# Goalkeeper location in orange
x_gk = df_optimal.at[i, 'x_gk']
y_gk = df_optimal.at[i, 'y_gk']
plt.scatter(x_gk, y_gk)

# TOGKP in orange
x_opt = df_optimal.at[i, 'x_opt']
y_opt = df_optimal.at[i, 'y_opt']
plt.scatter(x_opt, y_opt)

# Post location in red
x_p = cfg.df_posts['x']
y_p = cfg.df_posts['y']
plt.scatter(x_p, y_p)

# Plot line between shot location and gp1
point1 = df_optimal.at[i, 'location']
point2 = [120, 36]

x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]

plt.plot(x_values, y_values)

# Plot line between shot location and gp2
point1 = df_optimal.at[i, 'location']
point2 = [120, 44]

x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]

plt.plot(x_values, y_values)

# Plot bisector
point1 = df_optimal.at[i, 'location']
point2 = [x_opt, y_opt]

x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]

plt.plot(x_values, y_values)

# Display plot
plt.show()



for i in range(0, len(df_optimal)):
    # Player location in blue
    x = df_optimal.at[i, 'x_s']
    y = df_optimal.at[i, 'y_s']
    plt.scatter(x, y)

# Post location in green
x_p = cfg.df_posts['x']
y_p = cfg.df_posts['y']
plt.scatter(x_p, y_p)
    
# Display plot
plt.show()