def convex_hull(points):

    points = sorted(points)
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    # build the lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    # build the upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # remove the last point of each half because & remove the repeatd values in the other side
    return lower[:-1] + upper[:-1]

def main():
    # input (e.g., (0, 3) (2, 2) (1, 1))
    input_str = input("Input:")
    # Parse the input
    points = []
    for p in input_str.split():
        x, y = map(int, p.strip('()').split(','))
        points.append((x, y))
    # Find the convex hull
    hull = convex_hull(points)
    # Print the result
    print("Output", hull)

if __name__ == "__main__":
    main()
