def population_density(mass, volume):
    test1 = mass/volume
    expected_result = 10
    print("expected result: {}, actual result: {}\n".format(expected_result, test1))

def population_density2(mass, volume):
    test2 = mass/volume
    expected_result2 = 7123.6902801
    print("expected result: {}, actual result: {}".format(expected_result2, test2))


population_density(10, 1)
population_density2(864816, 121.4)