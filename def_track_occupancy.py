def number(bus_stops):
    net = []
    for x in bus_stops:
        diff = x[0]-x[1]
        net.append(diff)
    return sum(net)


# Better Solution:
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])