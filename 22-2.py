# On May 19, 2020, the New York Times reported a 123% increase in U.S. air
# travel in a single month (from 95,161 passengers to 212,508 passengers).
# It also reported that this increase followed a recent 96% drop in air
# travel. What was the total net percentage change?

x = 95161 * (1 / (1 - 0.96))
y = (212508 - x) / x

percent_change = 100 * y

print(percent_change, "%")
