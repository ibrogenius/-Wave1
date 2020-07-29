#Lab1of3
reservoir_volume = 4.445 * 10 ** 8
rainfall = 5 * 10 ** 6
#decreasing the rainfall by 10% which will be 0.1 as instructed
rainfall -= rainfall * 0.1
#adding the rainfall and reservoir_volume
reservoir_volume += rainfall
#increasing the reservoir volume by 5%
reservoir_volume += reservoir_volume * 0.05
#decreasing the reservoir volume by another 5%
reservoir_volume -= reservoir_volume * 0.05
#substracting 2.5e5
reservoir_volume -= 2.5 * 10 ** 5

print(reservoir_volume)