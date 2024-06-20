import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import cycle

def continued_fraction_sqrt(n, max_length=20):
    """Compute the continued fraction representation of the square root of an integer."""
    m, d, a0 = 0, 1, int(math.sqrt(n))
    a = a0
    cf = [a]

    if a * a == n:
        return cf  # Terminate if n is a perfect square

    for _ in range(1, max_length):
        m = d * a - m
        d = (n - m * m) / d
        a = int((a0 + m) / d)
        cf.append(a)

    return cf

def plot_incremental_steps(sequences, custom_sequences=None, node_size=5, target_x=None, coordinates=None):
    plt.figure(figsize=(12, 8))
    color_cycle = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
    
    # Determine plot range if coordinates are provided
    if coordinates:
        x_min, x_max, y_min, y_max = coordinates
    elif target_x:
        x_min, x_max = 0, target_x
        y_min, y_max = None, None  # Auto-scale y-axis based on data
    else:
        x_min, x_max, y_min, y_max = None, None, None, None

    def compute_angles(x, y):
        angles = []
        for i in range(1, len(x)):
            dx = x[i] - x[0]
            dy = y[i] - y[0]
            angle = np.arctan2(dy, dx) * (180 / np.pi)
            angles.append(angle)
        return angles

    all_angles = []

    for seq in sequences:
        color = next(color_cycle)
        x, y = [0], [0]  # Starting points
        step_count = 0
        for index, value in enumerate(seq):
            direction = 1 if index % 2 == 0 else -1
            for _ in range(value):
                if target_x and step_count >= target_x:
                    break  # Stop if reached target_x
                x.append(x[-1] + 1)
                y.append(y[-1] + direction)
                step_count += 1
        angles = compute_angles(x, y)
        all_angles.extend(angles)
        plt.plot(x, y, marker='o', linestyle='-', color=color, markersize=node_size)

    if custom_sequences:
        for custom_seq in custom_sequences:  # Iterate over multiple custom sequences
            color = next(color_cycle)
            x, y = [0], [0]
            step_count = 0
            for index, value in enumerate(custom_seq):
                direction = 1 if index % 2 == 0 else -1
                for _ in range(value):
                    if target_x and step_count >= target_x:
                        break
                    x.append(x[-1] + 1)
                    y.append(y[-1] + direction)
                    step_count += 1
            angles = compute_angles(x, y)
            all_angles.extend(angles)
            plt.plot(x, y, marker='o', linestyle='--', color=color, markersize=node_size)

    if any(v is not None for v in [x_min, x_max, y_min, y_max]):
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)

    mean_angle = np.mean(all_angles)
    plt.title(f'Incremental Steps for Each Number in Sequences\nMean Angle: {mean_angle:.2f}°')
    plt.xlabel('Step')
    plt.ylabel('Position')
    plt.grid(True)
    plt.show()

# Example usage
input_numbers = list(range(1, 2))  # Example range
sequences = [continued_fraction_sqrt(n) for n in input_numbers]

# Including multiple custom sequences

custom_sequences = [
    [1, 2, 1, 1, 8, 1, 1, 14, 1, 1, 20, 1, 1, 26, 1, 1, 32, 1, 1, 38, 1, 1, 44, 1, 1, 50, 1, 1, 56, 1, 1, 62, 1, 1, 68, 1, 1, 74, 1, 1, 80, 1, 1, 86, 1, 1, 92, 1, 1, 98, 1, 1, 104, 1, 1, 110, 1, 1, 116, 1, 1, 122, 1, 1, 128, 1, 1, 134, 1, 1, 140, 1, 1, 146, 1, 1, 152, 1, 1, 158, 1, 1, 164, 1, 1, 170, 1, 1, 176, 1, 1, 182, 1, 1, 188, 1, 1, 194, 1, 1, 200, 1, 1, 206, 1, 1, 212, 1, 1, 218, 1, 1, 224, 1, 1, 230, 1, 1, 236, 1, 1, 242, 1, 1, 248, 1, 1, 254, 1, 1, 260, 1, 1, 266, 1, 1, 272, 1, 1, 278, 1, 1, 284, 1, 1, 290, 1, 1, 296, 1, 1, 302, 1, 1, 308, 1, 1, 314, 1, 1, 320, 1, 1, 326, 1, 1, 332, 1, 1, 338, 1, 1, 344, 1, 1, 350, 1, 1, 356, 1, 1, 362, 1, 1, 368, 1, 1, 374, 1, 1, 380, 1, 1, 386, 1, 1, 392, 1, 1, 398, 1, 1, 404, 1, 1, 410, 1, 1, 416, 1, 1, 422, 1, 1, 428, 1, 1, 434, 1, 1, 440, 1, 1, 446, 1, 1, 452, 1, 1, 458, 1, 1, 464, 1, 1, 470, 1, 1, 476, 1, 1, 482, 1, 1, 488, 1, 1, 494, 1, 1, 500, 1, 1, 506, 1, 1, 512, 1, 1, 518, 1, 1, 524, 1, 1, 530, 1, 1, 536, 1, 1, 542, 1, 1, 548, 1, 1, 554, 1, 1, 560, 1, 1, 566, 1, 1, 572, 1, 1, 578, 1, 1, 584, 1, 1, 590, 1, 1, 596, 1, 1, 602, 1, 1, 608, 1, 1, 614, 1, 1, 620, 1, 1, 626, 1, 1, 632, 1, 1, 638, 1, 1, 644, 1, 1, 650, 1, 1, 656, 1, 1, 662, 1, 1, 668, 1, 1, 674, 1, 1, 680, 1, 1, 686, 1, 1, 692, 1, 1, 698, 1, 1, 704, 1, 1, 710, 1, 1, 716, 1, 1, 722, 1, 1, 728, 1, 1, 734, 1, 1, 740, 1, 1, 746, 1, 1, 752, 1, 1, 758, 1, 1, 764, 1, 1, 770, 1, 1, 776, 1, 1, 782, 1, 1, 788, 1, 1, 794, 1, 1, 800, 1, 1, 806, 1, 1, 812, 1, 1, 818, 1, 1, 824, 1, 1, 830, 1, 1, 836, 1, 1, 842, 1, 1, 848, 1, 1, 854, 1, 1, 860, 1, 1, 866, 1, 1, 872, 1, 1, 878, 1, 1, 884, 1, 1, 890, 1, 1, 896, 1, 1, 902, 1, 1, 908, 1, 1, 914, 1, 1, 920, 1, 1, 926, 1, 1, 932, 1, 1, 938, 1, 1, 944, 1, 1, 950, 1, 1, 956, 1, 1, 962, 1, 1, 968, 1, 1, 974, 1, 1, 980, 1, 1, 986, 1, 1, 992, 1, 1, 998, 1, 1, 1004, 1, 1, 1010, 1, 1, 1016, 1, 1, 1022, 1, 1, 1028, 1, 1, 1034, 1, 1, 1040, 1, 1, 1046, 1, 1, 1052, 1, 1, 1058, 1, 1, 1064, 1, 1, 1070, 1, 1, 1076, 1, 1, 1082, 1, 1, 1088, 1, 1, 1094, 1, 1, 1100, 1, 1, 1106, 1, 1, 1112, 1, 1, 1118, 1, 1, 1124, 1, 1, 1130, 1, 1, 1136, 1, 1, 1142, 1, 1, 1148, 1, 1, 1154, 1, 1, 1160, 1, 1, 1166, 1, 1, 1172, 1, 1, 1178, 1, 1, 1184, 1, 1, 1190, 1, 1, 1196, 1, 1, 1202, 1, 1, 1208, 1, 1, 1214, 1, 1, 1220, 1, 1, 1226, 1, 1, 1232, 1, 1, 1238, 1, 1, 1244, 1, 1, 1250, 1, 1, 1256, 1, 1, 1262, 1, 1, 1268, 1, 1, 1274, 1, 1, 1280, 1, 1, 1286, 1, 1, 1292, 1, 1, 1298, 1, 1, 1304, 1, 1, 1310, 1, 1, 1316, 1, 1, 1322, 1, 1, 1328, 1, 1, 1334, 1, 1, 1340, 1, 1, 1346, 1, 1, 1352, 1, 1, 1358, 1, 1, 1364, 1, 1, 1370, 1, 1, 1376, 1, 1, 1382, 1, 1, 1388, 1, 1, 1394, 1, 1, 1400, 1, 1, 1406, 1, 1, 1412, 1, 1, 1418, 1, 1, 1424, 1, 1, 1430, 1, 1, 1436, 1, 1, 1442, 1, 1, 1448, 1, 1, 1454, 1, 1, 1460, 1, 1, 1466, 1, 1, 1472, 1, 1, 1478, 1, 1, 1484, 1, 1, 1490, 1, 1, 1496, 1, 1, 1502, 1, 1, 1508, 1, 1, 1514, 1, 1, 1520, 1, 1, 1526, 1, 1, 1532, 1, 1, 1538, 1, 1, 1544, 1, 1, 1550, 1, 1, 1556, 1, 1, 1562, 1, 1, 1568, 1, 1, 1574, 1, 1, 1580, 1, 1, 1586, 1, 1, 1592, 1, 1, 1598, 1, 1, 1604, 1, 1, 1610, 1, 1, 1616, 1, 1, 1622, 1, 1, 1628, 1, 1, 1634, 1, 1, 1640, 1, 1, 1646, 1, 1, 1652, 1, 1, 1658, 1, 1, 1664, 1, 1, 1670, 1, 1, 1676, 1, 1, 1682, 1, 1, 1688, 1, 1, 1694, 1, 1, 1700, 1, 1, 1706, 1, 1, 1712, 1, 1, 1718, 1, 1, 1724, 1, 1, 1730, 1, 1, 1736, 1, 1, 1742, 1, 1, 1748, 1, 1, 1754, 1, 1, 1760, 1, 1, 1766, 1, 1, 1772, 1, 1, 1778, 1, 1, 1784, 1, 1, 1790, 1, 1, 1796, 1, 1, 1802, 1, 1, 1808, 1, 1, 1814, 1, 1, 1820, 1, 1, 1826, 1, 1, 1832, 1, 1, 1838, 1, 1, 1844, 1, 1, 1850, 1, 1, 1856, 1, 1, 1862, 1, 1, 1868, 1, 1, 1874, 1, 1, 1880, 1, 1, 1886, 1, 1, 1892, 1, 1, 1898, 1, 1, 1904, 1, 1, 1910, 1, 1, 1916, 1, 1, 1922, 1, 1, 1928, 1, 1, 1934, 1, 1, 1940, 1, 1, 1946, 1, 1, 1952, 1, 1, 1958, 1, 1, 1964, 1, 1, 1970, 1, 1, 1976, 1, 1, 1982, 1, 1, 1988, 1, 1, 1994, 1, 1, 2000, 1, 1, 2006, 1, 1, 2012, 1, 1, 2018, 1, 1, 2024, 1, 1, 2030, 1, 1, 2036, 1, 1, 2042, 1, 1, 2048, 1, 1, 2054, 1, 1, 2060, 1, 1, 2066, 1, 1, 2072, 1, 1, 2078, 1, 1, 2084, 1, 1, 2090, 1, 1, 2096, 1, 1, 2102, 1, 1, 2108, 1, 1, 2114, 1, 1, 21] ,


]  

# Example of customizing plot features
plot_incremental_steps(sequences, custom_sequences, node_size=0.2, target_x=10000)
