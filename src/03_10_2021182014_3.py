import math

# Original list of coordinate tuples
original_coords = [
    (527, 416), (471, 625), (880, 13), (1163, 145), (1426, 806),
    (14, 429), (742, 531), (1037, 630), (1025, 879), (377, 257),
    (614, 553), (481, 676), (943, 53), (88, 9), (28, 271),
    (952, 279), (1426, 519), (699, 698), (925, 716), (1132, 414),
    (1371, 238), (1389, 689), (1573, 774), (915, 636), (941, 763),
    (1083, 385), (1297, 588), (764, 389), (1536, 186), (1098, 515),
    (1308, 65), (1111, 550), (566, 422), (124, 105), (620, 332),
    (784, 623), (182, 555), (1413, 451), (1092, 660), (30, 217),
    (525, 148), (1311, 887), (1228, 353), (54, 68), (1155, 838),
]

coords = [list(t) + [i] for i, t in enumerate(original_coords)]

def dist(a, b):
    dx, dy = a[0] - b[0], a[1] - b[1]
    return math.sqrt(dx ** 2 + dy ** 2)

def dist_sq(a, b):
    dx, dy = a[0] - b[0], a[1] - b[1]
    return dx ** 2 + dy ** 2

def brute_force(array, left, right):
    min_dist = [-1, -1, float('inf')]
    for i1 in range(left, right + 1):
        c1 = array[i1]
        for i2 in range(i1 + 1, right + 1):
            c2 = array[i2]
            distance = dist(c1, c2)
            if distance < min_dist[2]:
                min_dist = [c1[2], c2[2], distance]
    return min_dist

def brute_all():
    s, e, d = brute_force(coords, 0, len(coords) - 1)
    return s, e, d



def devide_and_conquer():
    sorted_by_x = sorted(coords, key=lambda c: c[0])


    sorted_by_y = sorted(coords, key=lambda c: c[1])


    s, e, d = closest_pair(sorted_by_x, sorted_by_y, 0, len(sorted_by_x) - 1)
    return s, e, d

def closest_pair(arr_sorted_x, arr_sorted_y, left, right):
    """Recursively find the closest pair of points."""
    size = right - left + 1


    if size <= 1:
        return -1, -1, float('inf')  
    if size == 2:
        s, e = arr_sorted_x[left][2], arr_sorted_x[right][2]
        d = dist(arr_sorted_x[left], arr_sorted_x[right])
        return s, e, d
    if size == 3:
        s, e, d = brute_force(arr_sorted_x, left, right)
        return s, e, d

    mid = left + size // 2
    mid_point = arr_sorted_x[mid]


    left_y = []
    right_y = []
    for point in arr_sorted_y:
        if point[0] < mid_point[0] or (point[0] == mid_point[0] and point[2] <= mid):
            left_y.append(point)
        else:
            right_y.append(point)


    ls, le, ld = closest_pair(arr_sorted_x, left_y, left, mid - 1)
    rs, re, rd = closest_pair(arr_sorted_x, right_y, mid, right)


    if ld <= rd:
        s, e, d = ls, le, ld
    else:
        s, e, d = rs, re, rd

    strip = [point for point in arr_sorted_y if abs(point[0] - mid_point[0]) < d]
    n_strip = len(strip)


    for i in range(n_strip):
        for j in range(i + 1, n_strip):
            if (strip[j][1] - strip[i][1]) >= d:
                break  
            distance = dist(strip[i], strip[j])
            if distance < d:
                d = distance
                s, e = strip[i][2], strip[j][2]

    return s, e, d

def main():

    s, e, d = devide_and_conquer()

    print(f'{s=} {e=} {d=}')
    print(f'[{s}]{coords[s]} - [{e}]{coords[e]}, {d=}')

if __name__ == "__main__":
    main()
