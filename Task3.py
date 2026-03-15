#Task 3
#100500474

import math

def distance(a, b):
    lat1 = float(a[1])
    lon1 = float(a[2])
    lat2 = float(b[1])
    lon2 = float(b[2])

    dx = (lon2 - lon1) * 111412
    dy = (lat2 - lat1) * 111132

    return math.sqrt(dx * dx + dy * dy)


def bubble_sort(nodes, destination):
    n = len(nodes)

    for i in range(n):
        for j in range(0, n - i - 1):

            d1 = distance(nodes[j], destination)
            d2 = distance(nodes[j + 1], destination)

            if d1 > d2:
                temp = nodes[j]
                nodes[j] = nodes[j + 1]
                nodes[j + 1] = temp
            
            # tie-break by name
            elif d1 == d2:                                             
                if nodes[j][0] > nodes[j + 1][0]:
                    temp = nodes[j]
                    nodes[j] = nodes[j + 1]
                    nodes[j + 1] = temp


def path_builder(data, origin, destination, drone_range):

    nodes = data.copy()
    bubble_sort(nodes, destination)

    path = []
    visited = []

    current = origin

    path.append((current[0], None))
    visited.append(current)

    while True:

        # check if destination reachable directly
        if distance(current, destination) <= drone_range:
            path.append((destination[0], "DEST"))
            break

        moved = False

        for k in range(len(nodes)):

            node = nodes[k]

            if node in visited:
                continue

            if distance(current, node) <= drone_range:
                path.append((node[0], k))
                visited.append(node)
                current = node
                moved = True
                break

        if not moved:
            break

    return path

# Data provided

data = [["Warehouse_Zone3_0", 41.312, 3.185, 38, "Loading"], ["Repair_Center_Zone2_1", 44.85, 13.7, 53, "Unloading"], ["Repair_Center_Zone3_2", 41.727, 3.386, 91, "Loading"],
  ["Store_Zone2_3", 44.289, 13.5, 15, "Unloading"], ["Office_Zone2_4", 45.278, 13.228, 17, "Loading"], ["Office_Zone2_5", 45.183, 13.582, 26, "Unloading"],
  ["Farm_Zone3_6", 41.476, 3.028, 67, "Loading"], ["Warehouse_Zone3_7", 41.193, 3.235, 21, "Unloading"], ["Store_Zone1_8", 40.741, -9.308, 16, "Loading"],
  ["Store_Zone2_9", 45.554, 13.714, 22, "Unloading"], ["Store_Zone1_10", 40.793, -9.275, 48, "Loading"], ["Store_Zone3_11", 41.54, 3.566, 68, "Unloading"],
  ["Farm_Zone2_12", 45.894, 13.366, 43, "Loading"], ["Warehouse_Zone3_13", 41.036, 3.507, 3, "Unloading"], ["Factory_Zone1_14", 40.19, -9.038, 72, "Loading"],
  ["Store_Zone1_15", 40.593, -9.654, 2, "Unloading"], ["Factory_Zone3_16", 41.116, 3.675, 80, "Loading"], ["Train_Station_Zone1_17", 40.222, -9.503, 11, "Unloading"],
  ["Factory_Zone3_18", 41.898, 3.246, 88, "Loading"], ["High_Rise_Building_Zone1_19", 40.577, -9.098, 45, "Unloading"], ["Factory_Zone1_20", 40.904, -9.837, 21, "Loading"],
  ["Depot_Zone3_21", 41.265, 3.045, 46, "Unloading"], ["Office_Zone2_22", 45.888, 13.649, 78, "Loading"], ["Post_Office_Zone1_23", 40.171, -9.263, 3, "Unloading"],
  ["Repair_Center_Zone3_24", 41.531, 3.968, 29, "Loading"], ["Warehouse_Zone1_25", 40.76, -9.399, 54, "Unloading"], ["Farm_Zone3_26", 41.155, 3.916, 86, "Loading"],
  ["Farm_Zone2_27", 44.478, 13.513, 12, "Unloading"], ["Depot_Zone2_28", 45.329, 13.053, 1, "Loading"], ["Factory_Zone3_29", 41.936, 3.079, 1, "Unloading"],
  ["Farm_Zone1_30", 40.731, -9.512, 21, "Loading"], ["Suburban_House_Zone2_31", 44.777, 13.771, 71, "Unloading"], ["Train_Station_Zone2_32", 45.367, 13.245, 54, "Loading"],
  ["Farm_Zone1_33", 40.43, "-9.651", 1, "Unloading"], ["Suburban_House_Zone1_34", 40.546, -9.138, 60, "Loading"], ["Store_Zone1_35", 40.785, -9.569, 72, "Unloading"],
  ["High_Rise_Building_Zone2_36", 45.887, 13.12, 59, "Loading"], ["Depot_Zone2_37", 45.826, 13.665, 49, "Unloading"], ["Repair_Center_Zone3_38", 41.968, 3.545, 42, "Loading"],
  ["Store_Zone2_39", 45.673, 13.102, 32, "Unloading"], ["Train_Station_Zone1_40", 40.909, -9.896, 8, "Loading"], ["Office_Zone1_41", 40.861, -9.169, 19, "Unloading"],
  ["Warehouse_Zone3_42", 41.93, 3.705, 56, "Loading"], ["Repair_Center_Zone1_43", 40.259, -9.226, 36, "Unloading"], ["Post_Office_Zone2_44", 45.162, 13.716, 63, "Loading"],
  ["Office_Zone3_45", 41.12, 3.797, 63, "Unloading"], ["Factory_Zone3_46", 41.418, 3.774, 35, "Loading"], ["Suburban_House_Zone3_47", 41.047, 3.498, 97, "Unloading"],
  ["Warehouse_Zone3_48", 41.855, 3.014, 48, "Loading"], ["Suburban_House_Zone1_49", 40.349, -9.124, 76, "Unloading"], ["Factory_Zone2_50", 44.092, 13.601, 85, "Loading"],
  ["Store_Zone2_51", 44.806, 13.296, 56, "Unloading"], ["High_Rise_Building_Zone3_52", 41.12, 3.317, 24, "Loading"], ["Office_Zone2_53", 45.77, 13.6, 52, "Unloading"],
  ["Warehouse_Zone3_54", 41.614, 3.08, 34, "Loading"], ["Office_Zone2_55", 44.147, 13.009, 88, "Unloading"], ["Farm_Zone2_56", 44.514, 13.165, 93, "Loading"],
  ["Factory_Zone3_57", 41.07, 3.928, 24, "Unloading"], ["Train_Station_Zone1_58", 40.607, -9.354, 27, "Loading"], ["Warehouse_Zone3_59", 41.155, 3.45, 71, "Unloading"],
  ["Post_Office_Zone2_60", 45.623, 13.03, 92, "Loading"], ["Store_Zone3_61", 41.51, 3.641, 94, "Unloading"], ["Suburban_House_Zone3_62", 41.3, 3.028, 71, "Loading"],
  ["Factory_Zone3_63", 41.184, 3.625, 97, "Unloading"], ["Repair_Center_Zone2_64", 45.017, 13.853, 53, "Loading"], ["Farm_Zone1_65", 40.871, -9.465, 70, "Unloading"],
  ["Depot_Zone2_66", 45.836, 13.024, 67, "Loading"], ["Farm_Zone2_67", 45.186, 13.076, 73, "Unloading"], ["High_Rise_Building_Zone3_68", 41.468, 3.382, 84, "Loading"],
  ["Post_Office_Zone2_69", 44.921, 13.305, 29, "Unloading"], ["Repair_Center_Zone3_70", 41.961, 3.94, 94, "Loading"], ["Warehouse_Zone3_71", 41.654, 3.108, 42, "Unloading"],
  ["Store_Zone1_72", 40.712, -9.002, 39, "Loading"], ["Farm_Zone1_73", 40.602, -9.878, 18, "Unloading"], ["Depot_Zone2_74", 45.7, 13.16, 26, "Loading"],
  ["Repair_Center_Zone3_75", 41.052, 3.195, 36, "Unloading"], ["Train_Station_Zone1_76", 40.464, -9.145, 41, "Loading"], ["Train_Station_Zone1_77", 40.757, -9.425, 97, "Unloading"],
  ["Store_Zone1_78", 40.521, -9.049, 16, "Loading"], ["Post_Office_Zone2_79", 45.788, 13.998, 28, "Unloading"], ["Factory_Zone3_80", 41.384, 3.88, 4, "Loading"],
  ["Train_Station_Zone3_81", 41.336, 3.692, 41, "Unloading"], ["Suburban_House_Zone1_82", 40.919, -9.32, 34, "Loading"], ["High_Rise_Building_Zone2_83", 45.536, 13.786, 72, "Unloading"],
  ["Suburban_House_Zone1_84", 40.482, -9.314, 68, "Loading"], ["Train_Station_Zone3_85", 41.87, 3.649, 51, "Unloading"], ["Post_Office_Zone2_86", 45.673, 13.023, 0, "Loading"],
  ["Store_Zone3_87", 41.248, 3.314, 40, "Unloading"], ["Warehouse_Zone1_88", 40.658, -9.457, 71, "Loading"], ["Depot_Zone3_89", 41.561, 3.186, 80, "Unloading"],
  ["Warehouse_Zone2_90", 44.865, 13.805, 45, "Loading"], ["Factory_Zone3_91", 41.343, 3.586, 75, "Unloading"], ["Office_Zone1_92", 40.686, -9.56, 7, "Loading"],
  ["Office_Zone3_93", 41.476, 3.606, 13, "Unloading"], ["Depot_Zone1_94", 40.709, -9.341, 73, "Loading"], ["Depot_Zone2_95", 45.886, 13.391, 66, "Unloading"],
  ["High_Rise_Building_Zone2_96", 44.282, 13.597, 53, "Loading"], ["Repair_Center_Zone1_97", 40.005, -9.279, 90, "Unloading"], ["Farm_Zone2_98", 44.29, 13.029, 46, "Loading"],
  ["Office_Zone1_99", 40.522, -9.46, 88, "Unloading"], ["Factory_Zone3_100", 41.06, 3.979, 43, "Loading"], ["Factory_Zone3_101", 41.784, 3.924, 68, "Unloading"],
  ["Post_Office_Zone2_102", 45.848, 13.878, 3, "Loading"], ["Store_Zone1_103", 40.571, -9.787, 82, "Unloading"], ["Farm_Zone3_104", 41.767, 3.375, 25, "Loading"],
  ["Office_Zone1_105", 40.881, -9.36, 76, "Unloading"], ["Train_Station_Zone2_106", 44.879, 13.361, 10, "Loading"], ["Factory_Zone1_107", 40.527, -9.337, 78, "Unloading"],
  ["Suburban_House_Zone1_108", 40.736, -9.303, 15, "Loading"], ["Warehouse_Zone2_109", 45.538, 13.079, 60, "Unloading"], ["Suburban_House_Zone3_110", 41.867, 3.292, 95, "Loading"],
  ["Factory_Zone2_111", 44.37, 13.547, 12, "Unloading"], ["Repair_Center_Zone3_112", 41.525, 3.409, 12, "Loading"], ["Repair_Center_Zone2_113", 44.031, 13.894, 77, "Unloading"],
  ["Repair_Center_Zone3_114", 41.121, 3.06, 82, "Loading"], ["Repair_Center_Zone2_115", 44.223, 13.69, 58, "Unloading"], ["Post_Office_Zone1_116", 40.009, -9.265, 21, "Loading"],
  ["Repair_Center_Zone1_117", 40.804, -9.016, 17, "Unloading"], ["Warehouse_Zone1_118", 40.365, -9.294, 75, "Loading"], ["Warehouse_Zone3_119", 41.232, 3.213, 98, "Unloading"],
  ["Farm_Zone3_120", 41.43, 3.129, 93, "Loading"], ["Suburban_House_Zone2_121", 44.126, 13.926, 12, "Unloading"], ["Repair_Center_Zone3_122", 41.202, 3.292, 28, "Loading"],
  ["Repair_Center_Zone2_123", 45.675, 13.531, 86, "Unloading"], ["Warehouse_Zone1_124", 40.831, -9.981, 16, "Loading"], ["Warehouse_Zone2_125", 44.229, 13.14, 35, "Unloading"],
  ["Train_Station_Zone1_126", 40.839, -9.73, 72, "Loading"], ["High_Rise_Building_Zone3_127", 41.296, 3.161, 93, "Unloading"], ["Repair_Center_Zone3_128", 41.98, 3.067, 100, "Loading"],
  ["Warehouse_Zone1_129", 40.566, -9.522, 89, "Unloading"], ["High_Rise_Building_Zone3_130", 41.223, 3.495, 36, "Loading"], ["Train_Station_Zone2_131", 45.299, 13.072, 81, "Unloading"],
  ["High_Rise_Building_Zone2_132", 45.042, 13.612, 83, "Loading"], ["Factory_Zone1_133", 40.173, -9.26, 13, "Unloading"], ["Repair_Center_Zone3_134", 41.005, 3.197, 1, "Loading"],
  ["Warehouse_Zone1_135", 40.727, -9.445, 26, "Unloading"], ["Depot_Zone1_136", 40.998, -9.84, 81, "Loading"], ["Office_Zone3_137", 41.015, 3.326, 26, "Unloading"],
  ["High_Rise_Building_Zone2_138", 45.542, 13.48, 27, "Loading"], ["Post_Office_Zone1_139", 40.337, -9.463, 55, "Unloading"], ["Farm_Zone3_140", 41.114, 3.182, 26, "Loading"],
  ["Office_Zone1_141", 40.089, -9.153, 39, "Unloading"], ["Store_Zone1_142", 40.678, -9.652, 62, "Loading"], ["Factory_Zone1_143", 40.248, -9.681, 57, "Unloading"],
  ["Suburban_House_Zone1_144", 40.66, -9.736, 12, "Loading"], ["Office_Zone2_145", 45.824, 13.915, 56, "Unloading"], ["Train_Station_Zone3_146", 41.127, 3.238, 62, "Loading"],
  ["Repair_Center_Zone1_147", 40.986, -9.755, 29, "Unloading"], ["Train_Station_Zone1_148", 40.884, -9.778, 29, "Loading"], ["Suburban_House_Zone3_149", 41.583, 3.852, 20, "Unloading"],
  ["Train_Station_Zone1_150", 40.039, -9.382, 17, "Loading"], ["Warehouse_Zone3_151", 41.87, 3.11, 17, "Unloading"], ["Farm_Zone1_152", 40.11, -9.405, 80, "Loading"],
  ["Post_Office_Zone3_153", 41.66, 3.787, 83, "Unloading"], ["Suburban_House_Zone1_154", 40.494, -9.803, 21, "Loading"], ["Farm_Zone3_155", 41.88, 3.012, 74, "Unloading"],
  ["Repair_Center_Zone3_156", 41.107, 3.157, 62, "Loading"], ["Factory_Zone2_157", 45.685, 13.397, 68, "Unloading"], ["Depot_Zone2_158", 45.047, 13.88, 40, "Loading"],
  ["Suburban_House_Zone3_159", 41.6, 3.525, 78, "Unloading"], ["Repair_Center_Zone3_160", 41.906, 3.255, 53, "Loading"], ["Depot_Zone1_161", 40.276, -9.893, 17, "Unloading"],
  ["Farm_Zone2_162", 45.985, 13.033, 55, "Loading"], ["Office_Zone3_163", 41.471, 3.875, 6, "Unloading"], ["Suburban_House_Zone3_164", 41.059, 3.934, 3, "Loading"],
  ["High_Rise_Building_Zone1_165", 40.2, -9.113, 48, "Unloading"], ["High_Rise_Building_Zone3_166", 41.74, 3.0, 100, "Loading"], ["Repair_Center_Zone3_167", 41.107, 3.453, 39, "Unloading"],
  ["High_Rise_Building_Zone1_168", 40.619, -9.175, 11, "Loading"], ["Store_Zone3_169", 41.208, 3.057, 5, "Unloading"], ["Store_Zone1_170", 40.14, -9.242, 33, "Loading"],
  ["Post_Office_Zone2_171", 45.887, 13.739, 70, "Unloading"], ["Store_Zone1_172", 40.476, -9.155, 100, "Loading"], ["Office_Zone3_173", 41.729, 3.052, 14, "Unloading"],
  ["High_Rise_Building_Zone2_174", 45.499, 13.968, 76, "Loading"], ["Farm_Zone3_175", 41.584, 3.029, 61, "Unloading"], ["Repair_Center_Zone3_176", 41.412, 3.807, 34, "Loading"],
  ["Depot_Zone2_177", 44.017, 13.734, 70, "Unloading"], ["Factory_Zone3_178", 41.797, 3.901, 69, "Loading"], ["Repair_Center_Zone3_179", 41.357, 3.48, 67, "Unloading"],
  ["Warehouse_Zone1_180", 40.702, -9.248, 6, "Loading"], ["Post_Office_Zone1_181", 40.814, -9.205, 38, "Unloading"], ["Repair_Center_Zone3_182", 41.537, 3.222, 55, "Loading"],
  ["Factory_Zone2_183", 44.238, 13.79, 5, "Unloading"], ["Depot_Zone3_184", 41.836, 3.808, 5, "Loading"], ["Farm_Zone1_185", 40.789, -9.588, 17, "Unloading"],
  ["Store_Zone1_186", 40.82, -9.784, 69, "Loading"], ["Farm_Zone2_187", 45.882, 13.821, 62, "Unloading"], ["Train_Station_Zone1_188", 40.1, -9.094, 56, "Loading"],
  ["Post_Office_Zone3_189", 41.086, 3.116, 52, "Unloading"], ["Warehouse_Zone2_190", 44.853, 13.667, 16, "Loading"], ["Train_Station_Zone3_191", 41.941, 3.907, 77, "Unloading"],
  ["Depot_Zone3_192", 41.797, 3.323, 52, "Loading"], ["Office_Zone2_193", 45.756, 13.458, 35, "Unloading"], ["Farm_Zone2_194", 45.698, 13.531, 71, "Loading"],
  ["Store_Zone3_195", 41.99, 3.127, 99, "Unloading"], ["Warehouse_Zone2_196", 44.213, 13.633, 26, "Loading"], ["Farm_Zone2_197", 45.353, 13.663, 98, "Unloading"],
  ["Store_Zone3_198", 41.017, 3.538, 4, "Loading"], ["Repair_Center_Zone2_199", 45.046, 13.219, 97, "Unloading"], ["Farm_Zone1_200", 40.001, -9.142, 78, "Loading"],
  ["Suburban_House_Zone3_201", 41.829, 3.252, 53, "Unloading"], ["Office_Zone1_202", 40.584, -9.696, 30, "Loading"], ["Train_Station_Zone2_203", 45.255, 13.272, 8, "Unloading"],
  ["Store_Zone1_204", 40.166, -9.433, 15, "Loading"], ["High_Rise_Building_Zone1_205", 40.592, -9.625, 16, "Unloading"], ["Office_Zone2_206", 45.228, 13.032, 61, "Loading"],
  ["Suburban_House_Zone2_207", 45.807, 13.625, 32, "Unloading"], ["Warehouse_Zone2_208", 45.837, 13.869, 27, "Loading"], ["Warehouse_Zone3_209", 41.068, 3.847, 47, "Unloading"],
  ["High_Rise_Building_Zone3_210", 41.007, 3.227, 21, "Loading"], ["Office_Zone2_211", 45.635, 13.695, 48, "Unloading"], ["Post_Office_Zone1_212", 40.445, -9.127, 53, "Loading"],
  ["Warehouse_Zone1_213", 40.041, -9.148, 14, "Unloading"], ["Depot_Zone3_214", 41.363, 3.307, 94, "Loading"], ["Office_Zone2_215", 44.839, 13.484, 86, "Unloading"],
  ["Post_Office_Zone3_216", 41.276, 3.223, 61, "Loading"], ["Train_Station_Zone2_217", 45.671, 13.039, 100, "Unloading"], ["Post_Office_Zone2_218", 45.5, 13.644, 23, "Loading"],
  ["Office_Zone2_219", 45.401, 13.704, 72, "Unloading"], ["Office_Zone3_220", 41.663, 3.168, 39, "Loading"], ["Factory_Zone3_221", 41.646, 3.241, 33, "Unloading"],
  ["Suburban_House_Zone2_222", 44.261, 13.997, 54, "Loading"], ["Repair_Center_Zone3_223", 41.969, 3.475, 62, "Unloading"], ["Farm_Zone2_224", 45.781, 13.813, 21, "Loading"],
  ["Depot_Zone2_225", 45.424, 13.838, 70, "Unloading"], ["Office_Zone1_226", 40.618, -9.492, 58, "Loading"], ["Office_Zone1_227", 40.352, -9.517, 63, "Unloading"],
  ["Post_Office_Zone3_228", 41.255, 3.761, 55, "Loading"], ["Office_Zone3_229", 41.471, 3.688, 70, "Unloading"], ["High_Rise_Building_Zone1_230", 40.555, -9.632, 18, "Loading"],
  ["Suburban_House_Zone3_231", 41.39, 3.35, 4, "Unloading"], ["Suburban_House_Zone3_232", 41.822, 3.193, 96, "Loading"], ["Post_Office_Zone2_233", 45.467, 13.486, 70, "Unloading"],
  ["Train_Station_Zone2_234", 44.316, 13.537, 62, "Loading"], ["Repair_Center_Zone3_235", 41.283, 3.28, 47, "Unloading"], ["Office_Zone1_236", 40.701, -9.957, 53, "Loading"],
  ["High_Rise_Building_Zone3_237", 41.233, 3.849, 38, "Unloading"], ["Repair_Center_Zone1_238", 40.528, -9.116, 49, "Loading"], ["High_Rise_Building_Zone3_239", 41.513, 3.602, 70, "Unloading"],
  ["Depot_Zone1_240", 40.379, -9.098, 63, "Loading"], ["Suburban_House_Zone2_241", 45.276, 13.999, 93, "Unloading"], ["Farm_Zone2_242", 45.537, 13.664, 39, "Loading"],
  ["Warehouse_Zone3_243", 41.987, 3.042, 42, "Unloading"], ["Depot_Zone2_244", 44.704, 13.132, 98, "Loading"], ["Repair_Center_Zone3_245", 41.998, 3.706, 48, "Unloading"],
  ["Farm_Zone2_246", 45.938, 13.304, 23, "Loading"], ["Farm_Zone1_247", 40.066, -9.407, 72, "Unloading"], ["Farm_Zone2_248", 45.609, 13.494, 11, "Loading"],
  ["Train_Station_Zone2_249", 44.745, 13.936, 32, "Unloading"], ["Post_Office_Zone2_250", 44.091, 13.142, 46, "Loading"], ["Post_Office_Zone3_251", 41.69, 3.142, 8, "Unloading"],
  ["Office_Zone2_252", 44.338, 13.643, 79, "Loading"], ["Factory_Zone1_253", 40.731, -9.839, 84, "Unloading"], ["Suburban_House_Zone3_254", 41.275, 3.549, 12, "Loading"],
  ["Factory_Zone3_255", 41.505, 3.621, 6, "Unloading"], ["Depot_Zone1_256", 40.156, -9.554, 98, "Loading"], ["Depot_Zone3_257", 41.735, 3.044, 28, "Unloading"],
  ["Suburban_House_Zone1_258", 40.609, -9.349, 23, "Loading"], ["High_Rise_Building_Zone1_259", 40.025, -9.573, 69, "Unloading"], ["Office_Zone3_260", 41.318, 3.389, 52, "Loading"],
  ["Warehouse_Zone2_261", 44.642, 13.937, 68, "Unloading"], ["Store_Zone2_262", 44.933, 13.716, 78, "Loading"], ["Factory_Zone2_263", 44.215, 13.045, 43, "Unloading"],
  ["Factory_Zone3_264", 41.862, 3.23, 88, "Loading"], ["Store_Zone2_265", 45.007, 13.757, 33, "Unloading"], ["Factory_Zone1_266", 40.691, -9.745, 10, "Loading"],
  ["Repair_Center_Zone3_267", 41.502, 3.245, 5, "Unloading"], ["Post_Office_Zone2_268", 44.616, 13.939, 93, "Loading"], ["Store_Zone3_269", 41.085, 3.958, 55, "Unloading"],
  ["Store_Zone1_270", 40.956, -9.654, 21, "Loading"], ["Suburban_House_Zone2_271", 44.086, 13.524, 53, "Unloading"], ["Factory_Zone2_272", 44.072, 13.636, 36, "Loading"],
  ["Farm_Zone3_273", 41.138, 3.132, 55, "Unloading"], ["Office_Zone3_274", 41.362, 3.374, 9, "Loading"], ["Repair_Center_Zone2_275", 45.18, 13.345, 88, "Unloading"],
  ["Depot_Zone2_276", 44.767, 13.443, 24, "Loading"], ["Office_Zone1_277", 40.447, -9.161, 89, "Unloading"], ["Warehouse_Zone1_278", 40.083, -9.372, 40, "Loading"],
  ["Post_Office_Zone2_279", 44.919, 13.655, 76, "Unloading"], ["Train_Station_Zone3_280", 41.418, 3.568, 78, "Loading"], ["High_Rise_Building_Zone2_281", 45.168, 13.176, 7, "Unloading"],
  ["Store_Zone3_282", 41.246, 3.364, 92, "Loading"], ["Repair_Center_Zone1_283", 40.096, -9.621, 11, "Unloading"], ["Warehouse_Zone3_284", 41.012, 3.067, 94, "Loading"],
  ["High_Rise_Building_Zone2_285", 44.637, 13.943, 12, "Unloading"], ["Depot_Zone2_286", 45.038, 13.039, 11, "Loading"], ["Factory_Zone3_287", 41.159, 3.69, 35, "Unloading"],
  ["Office_Zone1_288", 40.396, -9.529, 28, "Loading"], ["Warehouse_Zone2_289", 45.305, 13.449, 45, "Unloading"], ["Repair_Center_Zone1_290", 40.375, -9.951, 41, "Loading"],
  ["Store_Zone2_291", 44.997, 13.956, 81, "Unloading"], ["Post_Office_Zone2_292", 45.32, 13.304, 10, "Loading"], ["Farm_Zone3_293", 41.491, 3.476, 5, "Unloading"],
  ["Repair_Center_Zone2_294", 45.397, 13.798, 69, "Loading"], ["Farm_Zone2_295", 44.204, 13.339, 81, "Unloading"], ["Farm_Zone2_296", 45.983, 13.089, 38, "Loading"],
  ["Office_Zone3_297", 41.277, 3.279, 71, "Unloading"], ["Warehouse_Zone3_298", 41.663, 3.055, 45, "Loading"], ["Depot_Zone2_299", 44.568, 13.365, 41, "Unloading"],
  ["High_Rise_Building_Zone3_300", 41.269, 3.842, 33, "Loading"], ["Suburban_House_Zone2_301", 45.485, 13.172, 91, "Unloading"], ["Farm_Zone2_302", 44.357, 13.136, 1, "Loading"],
  ["Warehouse_Zone3_303", 41.668, 3.806, 48, "Unloading"], ["Depot_Zone3_304", 41.561, 3.182, 25, "Loading"], ["Suburban_House_Zone2_305", 44.162, 13.544, 43, "Unloading"],
  ["Farm_Zone1_306", 40.577, -9.018, 72, "Loading"], ["Repair_Center_Zone2_307", 45.754, 13.998, 65, "Unloading"], ["Repair_Center_Zone2_308", 45.693, 13.844, 59, "Loading"],
  ["Factory_Zone3_309", 41.61, 3.847, 31, "Unloading"], ["Store_Zone1_310", 40.325, -9.377, 91, "Loading"], ["Farm_Zone3_311", 41.56, 3.777, 6, "Unloading"],
  ["Train_Station_Zone1_312", 40.522, -9.359, 14, "Loading"], ["Office_Zone2_313", 45.988, 13.902, 8, "Unloading"], ["Repair_Center_Zone1_314", 40.613, -9.983, 18, "Loading"],
  ["Store_Zone2_315", 44.794, 13.583, 27, "Unloading"], ["Train_Station_Zone3_316", 41.228, 3.086, 52, "Loading"], ["Repair_Center_Zone3_317", 41.622, 3.854, 69, "Unloading"],
  ["High_Rise_Building_Zone3_318", 41.684, 3.714, 14, "Loading"], ["Suburban_House_Zone3_319", 41.778, 3.594, 14, "Unloading"], ["Farm_Zone2_320", 44.584, 13.249, 37, "Loading"],
  ["Factory_Zone3_321", 41.252, 3.36, 97, "Unloading"], ["High_Rise_Building_Zone1_322", 40.863, -9.703, 72, "Loading"], ["Train_Station_Zone1_323", 40.436, -9.913, 32, "Unloading"],
  ["High_Rise_Building_Zone3_324", 41.718, 3.258, 64, "Loading"], ["High_Rise_Building_Zone3_325", 41.786, 3.06, 61, "Unloading"], ["High_Rise_Building_Zone3_326", 41.915, 3.448, 54, "Loading"],
  ["Store_Zone3_327", 41.942, 3.569, 10, "Unloading"], ["Depot_Zone2_328", 44.212, 13.607, 26, "Loading"], ["Farm_Zone3_329", 41.163, 3.841, 74, "Unloading"],
  ["Farm_Zone2_330", 44.259, 13.069, 31, "Loading"], ["Train_Station_Zone1_331", 40.606, -9.155, 79, "Unloading"], ["Farm_Zone3_332", 41.841, 3.739, 68, "Loading"],
  ["Suburban_House_Zone2_333", 45.495, 13.769, 19, "Unloading"], ["Post_Office_Zone1_334", 40.21, -9.798, 60, "Loading"], ["Repair_Center_Zone3_335", 41.571, 3.933, 39, "Unloading"],
  ["High_Rise_Building_Zone1_336", 40.913, -9.316, 79, "Loading"], ["Farm_Zone3_337", 41.477, 3.561, 46, "Unloading"], ["Store_Zone3_338", 41.274, 3.243, 40, "Loading"],
  ["Store_Zone2_339", 44.329, 13.988, 97, "Unloading"], ["High_Rise_Building_Zone2_340", 45.237, 13.416, 35, "Loading"], ["Suburban_House_Zone3_341", 41.683, 3.799, 13, "Unloading"],
  ["Train_Station_Zone2_342", 45.179, 13.617, 29, "Loading"], ["Store_Zone3_343", 41.947, 3.308, 79, "Unloading"], ["Repair_Center_Zone2_344", 45.909, 13.266, 1, "Loading"],
  ["Farm_Zone2_345", 45.608, 13.208, 83, "Unloading"], ["Store_Zone1_346", 40.763, -9.01, 4, "Loading"], ["Store_Zone2_347", 44.891, 13.036, 1, "Unloading"],
  ["High_Rise_Building_Zone1_348", 40.514, -9.164, 75, "Loading"], ["Post_Office_Zone3_349", 41.859, 3.808, 44, "Unloading"], ["Farm_Zone3_350", 41.025, 3.305, 16, "Loading"],
  ["Factory_Zone3_351", 41.364, 3.048, 87, "Unloading"], ["Office_Zone3_352", 41.47, 3.839, 51, "Loading"], ["High_Rise_Building_Zone2_353", 45.362, 13.484, 48, "Unloading"],
  ["Repair_Center_Zone1_354", 40.478, -9.958, 15, "Loading"], ["Depot_Zone3_355", 41.758, 3.908, 5, "Unloading"], ["Post_Office_Zone3_356", 41.909, 3.723, 29, "Loading"],
  ["Store_Zone3_357", 41.128, 3.919, 53, "Unloading"], ["Warehouse_Zone3_358", 41.021, 3.755, 66, "Loading"], ["Depot_Zone2_359", 44.566, 13.832, 48, "Unloading"],
  ["Warehouse_Zone3_360", 41.56, 3.125, 66, "Loading"], ["Post_Office_Zone1_361", 40.59, -9.438, 59, "Unloading"], ["Office_Zone1_362", 40.008, -9.068, 35, "Loading"],
  ["Warehouse_Zone2_363", 44.463, 13.414, 17, "Unloading"], ["Train_Station_Zone2_364", 45.672, 13.107, 39, "Loading"], ["Factory_Zone1_365", 40.267, -9.747, 78, "Unloading"],
  ["Farm_Zone1_366", 40.976, -9.203, 80, "Loading"], ["Warehouse_Zone2_367", 44.969, 13.501, 23, "Unloading"], ["Office_Zone3_368", 41.075, 3.013, 64, "Loading"],
  ["High_Rise_Building_Zone2_369", 44.817, 13.028, 6, "Unloading"], ["High_Rise_Building_Zone1_370", 40.196, -9.569, 10, "Loading"], ["Office_Zone1_371", 40.626, -9.018, 36, "Unloading"],
  ["High_Rise_Building_Zone1_372", 40.746, -9.069, 45, "Loading"], ["Factory_Zone3_373", 41.549, 3.158, 50, "Unloading"], ["Depot_Zone2_374", 44.932, 13.077, 22, "Loading"],
  ["Suburban_House_Zone1_375", 40.283, -9.52, 6, "Unloading"], ["Warehouse_Zone1_376", 40.884, -9.176, 74, "Loading"], ["Train_Station_Zone2_377", 45.242, 13.805, 96, "Unloading"],
  ["Store_Zone3_378", 41.755, 3.669, 91, "Loading"], ["Farm_Zone1_379", 40.122, -9.683, 69, "Unloading"], ["Post_Office_Zone1_380", 40.432, -9.58, 29, "Loading"],
  ["Repair_Center_Zone2_381", 45.755, 13.407, 58, "Unloading"], ["Factory_Zone1_382", 40.682, -9.245, 38, "Loading"], ["Post_Office_Zone3_383", 41.008, 3.103, 37, "Unloading"],
  ["Office_Zone2_384", 45.914, 13.645, 81, "Loading"], ["Office_Zone2_385", 44.981, 13.601, 93, "Unloading"], ["High_Rise_Building_Zone2_386", 44.82, 13.164, 7, "Loading"],
  ["Train_Station_Zone1_387", 40.158, -9.753, 64, "Unloading"], ["Store_Zone2_388", 45.898, 13.423, 70, "Loading"], ["Suburban_House_Zone3_389", 41.826, 3.396, 17, "Unloading"],
  ["Repair_Center_Zone2_390", 45.578, 13.47, 57, "Loading"], ["High_Rise_Building_Zone2_391", 45.126, 13.899, 55, "Unloading"], ["Repair_Center_Zone1_392", 40.432, -9.732, 4, "Loading"],
  ["Farm_Zone1_393", 40.033, -9.061, 13, "Unloading"], ["High_Rise_Building_Zone1_394", 40.921, -9.19, 60, "Loading"], ["Office_Zone1_395", 40.494, -9.322, 96, "Unloading"],
  ["Repair_Center_Zone1_396", 40.644, -9.914, 58, "Loading"], ["Repair_Center_Zone3_397", 41.544, 3.71, 100, "Unloading"], ["Depot_Zone1_398", 40.963, -9.972, 18, "Loading"],
  ["Warehouse_Zone3_399", 41.294, 3.174, 32, "Unloading"]]

origin = ["A", 41.0, 3.0, 10, "Loading"]
destination = ["Repair_Center_Zone3_397", 41.544, 3.71, 100, "Unloading"]
drone_range = 20000

result = path_builder(data, origin, destination, drone_range)

print("Route:")
for step in result:
    print(step)