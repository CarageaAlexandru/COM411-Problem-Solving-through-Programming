def cross_bridge(steps):
    if steps < 5:
        for steps in range(0, steps):
            print("Crossed step.")
        print("we must keep going")
    elif steps > 5:
        for steps in range(0, steps):
            print("Crossed step.")
        print("the bridge is collapsing!")

cross_bridge(3)
cross_bridge(6)