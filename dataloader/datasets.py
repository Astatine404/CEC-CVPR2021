# https://colab.research.google.com/drive/1MF4AIzDMkeOIFm1cpGouPNY92CBQHhsj?usp=sharing
custom_inc_classes = [[ 9, 10, 16, 28, 61],
                    [22, 39, 40, 86, 87],
                    [ 5, 20, 25, 84, 94],
                    [12, 17, 37, 68, 76],
                    [23, 33, 49, 60, 71],
                    [ 2, 11, 35, 46, 98],
                    [ 8, 13, 48, 58, 90],
                    [41, 69, 81, 85, 89]]

custom_base_classes = [0,  1,  3,  4,  6,  7, 14, 15, 18, 19, 21, 24, 26, 27, 29, 30, 31,
                    32, 34, 36, 38, 42, 43, 44, 45, 47, 50, 51, 52, 53, 54, 55, 56, 57,
                    59, 62, 63, 64, 65, 66, 67, 70, 72, 73, 74, 75, 77, 78, 79, 80, 82,
                    83, 88, 91, 92, 93, 95, 96, 97, 99]

class_map = dict(zip(custom_base_classes, list(range(len(custom_base_classes)))))
for session in range(len(custom_inc_classes)):
    classes_seen = len(custom_base_classes) + session * len(custom_inc_classes[session])
    class_map.update(dict(zip(custom_inc_classes[session], list(range(classes_seen, classes_seen + len(custom_inc_classes[session]))))))

custom_inc_classes_random = [[66, 32, 46, 28, 74],
                            [23, 10, 20, 17, 35],
                            [97, 37, 70, 40, 60],
                            [34, 42, 57, 12, 69],
                            [94, 56, 22, 39, 24],
                            [13, 63, 71, 55, 87],
                            [ 6, 88, 64, 26, 48],
                            [50, 72, 54, 21, 25]]

custom_base_classes_random = [ 0,  1,  2,  3,  4,  5,  7,  8,  9, 11, 14, 15, 16, 18, 19, 27, 29,
                            30, 31, 33, 36, 38, 41, 43, 44, 45, 47, 49, 51, 52, 53, 58, 59, 61,
                            62, 65, 67, 68, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                            89, 90, 91, 92, 93, 95, 96, 98, 99]

class_map_random = dict(zip(custom_base_classes_random, list(range(len(custom_base_classes_random)))))
for session in range(len(custom_inc_classes_random)):
    classes_seen = len(custom_base_classes_random) + session * len(custom_inc_classes_random[session])
    class_map_random.update(dict(zip(custom_inc_classes_random[session], list(range(classes_seen, classes_seen + len(custom_inc_classes_random[session]))))))

custom_inc_classes_random = [[66, 32, 46, 28, 74],
                            [23, 10, 20, 17, 35],
                            [97, 37, 70, 40, 60],
                            [34, 42, 57, 12, 69],
                            [94, 56, 22, 39, 24],
                            [13, 63, 71, 55, 87],
                            [ 6, 88, 64, 26, 48],
                            [50, 72, 54, 21, 25]]

custom_base_classes_random = [ 0,  1,  2,  3,  4,  5,  7,  8,  9, 11, 14, 15, 16, 18, 19, 27, 29,
                            30, 31, 33, 36, 38, 41, 43, 44, 45, 47, 49, 51, 52, 53, 58, 59, 61,
                            62, 65, 67, 68, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                            89, 90, 91, 92, 93, 95, 96, 98, 99]

class_map_random = dict(zip(custom_base_classes_random, list(range(len(custom_base_classes_random)))))
for session in range(len(custom_inc_classes_random)):
    classes_seen = len(custom_base_classes_random) + session * len(custom_inc_classes_random[session])
    class_map_random.update(dict(zip(custom_inc_classes_random[session], list(range(classes_seen, classes_seen + len(custom_inc_classes_random[session]))))))

custom_inc_classes_random_1 = [[80, 84, 33, 81, 93],
                                [17, 36, 82, 69, 65],
                                [92, 39, 56, 52, 51],
                                [32, 31, 44, 78, 10],
                                [ 2, 73, 97, 62, 19],
                                [35, 94, 27, 46, 38],
                                [67, 99, 54, 95, 88],
                                [40, 48, 59, 23, 34]]
custom_base_classes_random_1 = [ 0,  1,  3,  4,  5,  6,  7,  8,  9, 11, 12, 13, 14, 15, 16, 18, 20,
                                21, 22, 24, 25, 26, 28, 29, 30, 37, 41, 42, 43, 45, 47, 49, 50, 53,
                                55, 57, 58, 60, 61, 63, 64, 66, 68, 70, 71, 72, 74, 75, 76, 77, 79,
                                83, 85, 86, 87, 89, 90, 91, 96, 98]

custom_inc_classes_random_2 = [[83, 30, 56, 24, 16],
                                [23,  2, 27, 28, 13],
                                [99, 92, 76, 14,  0],
                                [21,  3, 29, 61, 79],
                                [35, 11, 84, 44, 73],
                                [ 5, 25, 77, 74, 62],
                                [65,  1, 18, 48, 36],
                                [78,  6, 89, 91, 10]]

custom_base_classes_random_2 = [ 4,  7,  8,  9, 12, 15, 17, 19, 20, 22, 26, 31, 32, 33, 34, 37, 38,
                                39, 40, 41, 42, 43, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 57, 58,
                                59, 60, 63, 64, 66, 67, 68, 69, 70, 71, 72, 75, 80, 81, 82, 85, 86,
                                87, 88, 90, 93, 94, 95, 96, 97, 98]

class_map_random_1 = dict(zip(custom_base_classes_random_1, list(range(len(custom_base_classes_random_1)))))
for session in range(len(custom_inc_classes_random_1)):
    classes_seen = len(custom_base_classes_random_1) + session * len(custom_inc_classes_random_1[session])
    class_map_random_1.update(dict(zip(custom_inc_classes_random_1[session], list(range(classes_seen, classes_seen + len(custom_inc_classes_random_1[session]))))))

class_map_random_2 = dict(zip(custom_base_classes_random_2, list(range(len(custom_base_classes_random_2)))))
for session in range(len(custom_inc_classes_random_2)):
    classes_seen = len(custom_base_classes_random_2) + session * len(custom_inc_classes_random_2[session])
    class_map_random_2.update(dict(zip(custom_inc_classes_random_2[session], list(range(classes_seen, classes_seen + len(custom_inc_classes_random_2[session]))))))

custom_inc_classes_superrandom_1 = [[ 9, 10, 16, 28, 61],
                                [36, 50, 65, 74, 80],
                                [ 5, 20, 25, 84, 94],
                                [23, 33, 49, 60, 71],
                                [54, 62, 70, 82, 92],
                                [ 2, 11, 35, 46, 98],
                                [ 0, 51, 53, 57, 83],
                                [47, 52, 56, 59, 96]]

custom_base_classes_superrandom_1 = [ 1,  3,  4,  6,  7,  8, 12, 13, 14, 15, 17, 18, 19, 21, 22, 24, 26,
                                    27, 29, 30, 31, 32, 34, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 55,
                                    58, 63, 64, 66, 67, 68, 69, 72, 73, 75, 76, 77, 78, 79, 81, 85, 86,
                                    87, 88, 89, 90, 91, 93, 95, 97, 99]

custom_inc_classes_superrandom_2 = [[34, 63, 64, 66, 75],
                                    [ 0, 51, 53, 57, 83],
                                    [ 8, 13, 48, 58, 90],
                                    [ 4, 30, 55, 72, 95],
                                    [12, 17, 37, 68, 76],
                                    [22, 39, 40, 86, 87],
                                    [ 9, 10, 16, 28, 61],
                                    [23, 33, 49, 60, 71]]

custom_base_classes_superrandom_2 = [ 1,  2,  3,  5,  6,  7, 11, 14, 15, 18, 19, 20, 21, 24, 25, 26, 27,
                                    29, 31, 32, 35, 36, 38, 41, 42, 43, 44, 45, 46, 47, 50, 52, 54, 56,
                                    59, 62, 65, 67, 69, 70, 73, 74, 77, 78, 79, 80, 81, 82, 84, 85, 88,
                                    89, 91, 92, 93, 94, 96, 97, 98, 99]

custom_inc_classes_superrandom_5 = [[54, 62, 70, 82, 92],
                                    [22, 39, 40, 86, 87],
                                    [47, 52, 56, 59, 96],
                                    [41, 69, 81, 85, 89],
                                    [34, 63, 64, 66, 75],
                                    [ 1, 32, 67, 73, 91],
                                    [15, 19, 21, 31, 38],
                                    [23, 33, 49, 60, 71]]

custom_base_classes_superrandom_5 = [ 0,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 16, 17, 18,
                                    20, 24, 25, 26, 27, 28, 29, 30, 35, 36, 37, 42, 43, 44, 45, 46, 48,
                                    50, 51, 53, 55, 57, 58, 61, 65, 68, 72, 74, 76, 77, 78, 79, 80, 83,
                                    84, 88, 90, 93, 94, 95, 97, 98, 99]


class_map_superrandom_1 = dict(zip(custom_base_classes_superrandom_1, list(range(len(custom_base_classes_superrandom_1)))))
for session in range(len(custom_inc_classes_superrandom_1)):
    classes_seen = len(custom_base_classes_superrandom_1) + session * len(custom_inc_classes_superrandom_1[session])
    class_map_superrandom_1.update(dict(zip(custom_inc_classes_superrandom_1[session], list(range(classes_seen, classes_seen + len(custom_inc_classes_superrandom_1[session]))))))

class_map_superrandom_2 = dict(zip(custom_base_classes_superrandom_2, list(range(len(custom_base_classes_superrandom_2)))))
for session in range(len(custom_inc_classes_superrandom_2)):
    classes_seen = len(custom_base_classes_superrandom_2) + session * len(custom_inc_classes_superrandom_2[session])
    class_map_superrandom_2.update(dict(zip(custom_inc_classes_superrandom_2[session], list(range(classes_seen, classes_seen + len(custom_inc_classes_superrandom_2[session]))))))

class_map_superrandom_5 = dict(zip(custom_base_classes_superrandom_5, list(range(len(custom_base_classes_superrandom_5)))))
for session in range(len(custom_inc_classes_superrandom_5)):
    classes_seen = len(custom_base_classes_superrandom_5) + session * len(custom_inc_classes_superrandom_5[session])
    class_map_superrandom_5.update(dict(zip(custom_inc_classes_superrandom_5[session], list(range(classes_seen, classes_seen + len(custom_inc_classes_superrandom_5[session]))))))
