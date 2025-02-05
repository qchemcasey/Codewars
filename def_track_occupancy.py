def number(bus_stops):
    net = []
    for x in bus_stops:
        diff = x[0]-x[1]
        net.append(diff)
    return sum(net)