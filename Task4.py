# Task 4 
# 100500474

import math

class Drone:

    # Initialiser
    def __init__(self, name, weight, maximum_energy):

        self.name = name
        self.weight = weight
        self.maximum_energy = maximum_energy
        self.current_energy = maximum_energy

        self.destinations = {}
        self.current_path = []


    #Getters
    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_current_energy(self):
        return self.current_energy

    def get_maximum_energy(self):
        return self.maximum_energy


    # Setters
    def set_name(self, n):
        self.name = n

    def set_weight(self, w):
        self.weight = w

    def set_current_energy(self, e):
        self.current_energy = e


    # Energy Calculation (Task 1 logic)
    def calculate_energy(self, m, p, h, V, b1_to, b0_to, b1_ld, b0_ld, b1_cr, b0_cr):

        E_to = (b1_to * (m**1.5 / math.sqrt(p)) + b0_to) * (h / V)
        E_ld = (b1_ld * (m**1.5 / math.sqrt(p)) + b0_ld) * (h / V)
        E_cr = (b1_cr * (m**1.5 / math.sqrt(p)) + b0_cr) * (h / V)

        return E_to + E_ld + E_cr

    # Range Calculation
    def calculate_range(self, energy_used, cruise_speed):

        if energy_used <= 0:
            return 0

        return (self.current_energy / energy_used) * cruise_speed


    # Load Destinations (Task 2 logic)
    def load_destinations(self, data_array):

        for item in data_array:

            name = item[0]
            lon = item[1]
            lat = item[2]
            alt = item[3]
            port = item[4]

            ok = True

            # Duplicate check
            if name in self.destinations:
                ok = False

            # Name check
            for c in name:
                if not (('A' <= c <= 'Z') or ('a' <= c <= 'z')
                        or ('0' <= c <= '9') or c == '_'):
                    ok = False

            # Convert numbers
            try:
                lon = float(lon)
                lat = float(lat)
                alt = float(alt)
            except:
                ok = False

            # Bounds
            if ok:
                if lon < -90 or lon > 90:
                    ok = False
                if lat < -90 or lat > 90:
                    ok = False
                if alt < 0 or alt > 100:
                    ok = False

            # Port check
            if port != "Loading" and port != "Unloading":
                ok = False

            # Store valid destination
            if ok:
                self.destinations[name] = [lon, lat, alt, port]


    # KNN Path Builder (Task 3 logic) 
    def update_path(self, origin, destination, drone_range):

        path = []

        origin_lon = origin[1]
        origin_lat = origin[2]

        dest_lon = destination[1]
        dest_lat = destination[2]

        # Distance from each node to destination
        nodes = []

        for name in self.destinations:

            lon, lat, alt, port = self.destinations[name]

            dx = (lon - dest_lon) * 111412
            dy = (lat - dest_lat) * 111132
            dist = math.sqrt(dx*dx + dy*dy)

            nodes.append((name, dist))

        # Simple Bubble Sort 
        for i in range(len(nodes)):
            for j in range(len(nodes)-1):
                if nodes[j][1] > nodes[j+1][1]:
                    nodes[j], nodes[j+1] = nodes[j+1], nodes[j]

        # Choose reachable nodes 
        K = 0

        for name, d in nodes:

            lon, lat, alt, port = self.destinations[name]

            dx = (lon - origin_lon) * 111412
            dy = (lat - origin_lat) * 111132
            dist_origin = math.sqrt(dx*dx + dy*dy)

            if dist_origin <= drone_range:
                path.append((name, K))
                origin_lon = lon
                origin_lat = lat

            K += 1

        self.current_path = path


    # Trip Feasibility Check 
    def check_trip(self, density, speed, b1_to, b0_to, b1_ld, b0_ld, b1_cr, b0_cr):

        energy_left = self.maximum_energy
        recharge_nodes = []

        for i in range(len(self.current_path) - 1):

            name1 = self.current_path[i][0]
            name2 = self.current_path[i+1][0]

            node1 = self.destinations[name1]
            node2 = self.destinations[name2]

            # Average altitude
            h = (node1[2] + node2[2]) / 2

            energy_needed = self.calculate_energy(
                self.weight, density, h, speed,
                b1_to, b0_to,
                b1_ld, b0_ld,
                b1_cr, b0_cr
            )

            if energy_needed > energy_left:
                recharge_nodes.append(name1)
                energy_left = self.maximum_energy

            energy_left -= energy_needed

        return recharge_nodes

# Data provided
data = [['Store_Zone1_0', '40.452', '-9.514', 300, 'Loading'], ['Depot_Zone2_1', 44.13, 13.966, 100, 'Unloading'], ['Warehouse_Zone3_2', 41.064, 3.819, 36, 'Loading'],
['Train_Station_Zone1_3', 40.612, -9.079, 4, 'Unloading'], ['Depot_Zone2_4', 44.246, 13.26, 5, 'Loading'], ['Office_Zone1_5', 40.447, '-9.674', 6, 'Unloading'],
['Repair_Center_Zone1_6', 40.025, -9.899, 82, 'Loading'], ['Warehouse_Zone2_7', 45.769, 13.21, 32, 'Unloading'], ['Post_Office_Zone3_8', 41.601, 3.046, 88, 'Loading'],
['Depot_Zone2_9', 45.538, 13.537, 98, 'Unloading'], ['Depot_Zone1_10', 40.246, '-9.984', 141, 'Loading'], ['Post_Office_Zone2_11', 44.181, 13.798, 54, 'Unloading'],
['Office_Zone2_12', 44.768, 13.747, 27, 'Loading'], ['Store_Zone2_13', 45.162, 13.864, 45, 'Unloading'], ['Warehouse_Zone1_14', 40.678, -9.074, 54, 'Loading'],
['Post_Office_Zone1_15', 40.277, '-9.753', 8, 'Unloading'], ['Suburban_House_Zone1_16', 40.398, -9.563, 19, 'Loading'], ['Post_Office_Zone1_17', 40.882, -9.698, 80, 'Unloading'],
['Farm_Zone1_18', 40.062, -9.926, 64, 'Loading'], ['Factory_Zone1_19', 40.966, -9.432, 65, 'Unloading'], ['Train_Station_Zone3_20', 41.912, '3.992', 288, 'Loading'],
['Suburban_House_Zone1_21', 40.72, -9.414, 83, 'Unloading'], ['Repair_Center_Zone1_22', 40.159, -9.192, 88, 'Loading'], ['Store_Zone3_23', 41.703, 3.329, 82, 'Unloading'],
['Store_Zone2_24', 44.742, 13.668, 85, 'Loading'], ['Repair_Center_Zone1_25', 40.898, '-9.83', 29, 'Unloading'], ['Repair_Center_Zone2_26', 45.469, 13.1, 32, 'Loading'],
['Train_Station_Zone1_27', 40.281, -9.36, 32, 'Unloading'], ['Train_Station_Zone3_28', 41.465, 3.377, 18, 'Loading'], ['Repair_Center_Zone3_29', 41.157, 3.5, 95, 'Unloading'],
['Repair_Center_Zone1_30', 40.047, '-9.387', 118, 'Loading'], ['Depot_Zone2_31', 45.415, 13.934, 86, 'Unloading'], ['Warehouse_Zone2_32', '44.958', 13.033, 57, 'Loading'],
['Warehouse_Zone3_33', 41.616, 3.444, 68, 'Unloading'], ['Farm_Zone3_34', 41.75, 3.91, 78, 'Loading'], ['Factory_Zone3_35', 41.469, '3.582', 38, 'Unloading'],
['Office_Zone3_36', 41.444, 3.438, 5, 'Loading'], ['Farm_Zone2_37', 45.304, 13.73, 38, 'Unloading'], ['Post_Office_Zone1_38', 40.257, -9.821, 62, 'Loading'],
['Depot_Zone2_39', 44.021, 13.171, 97, 'Unloading'], ['High_Rise_Building_Zone2_40', 44.613, '13.768', 293, 'Loading'], ['Warehouse_Zone2_41', 44.325, 13.76, 10, 'Unloading'],
['Post_Office_Zone3_42', 41.617, 3.252, 8, 'Loading'], ['High_Rise_Building_Zone3_43', 41.782, 3.297, 77, 'Unloading'], ['Train_Station_Zone3_44', 41.776, 3.506, 26, 'Loading'],
['Store_Zone1_45', 40.052, '-9.422', 34, 'Unloading'], ['Post_Office_Zone3_46', 41.633, 3.616, 59, 'Loading'], ['Suburban_House_Zone1_47', 40.905, -9.216, 75, 'Unloading'],
['Repair_Center_Zone1_48', 40.416, -9.087, 54, 'Loading'], ['Repair_Center_Zone2_49', 45.098, 13.906, 86, 'Unloading'], ['Repair_Center_Zone2_50', 45.159, '13.706', 261, 'Loading'],
['High_Rise_Building_Zone3_51', 41.657, 3.092, 52, 'Unloading'], ['Train_Station_Zone3_52', 41.902, 3.821, 86, 'Loading'], ['Depot_Zone1_53', 40.724, -9.113, 88, 'Unloading'],
['Post_Office_Zone2_54', 45.315, 13.913, 34, 'Loading'], ['Depot_Zone1_55', 40.878, '-9.871', 88, 'Unloading'], ['Suburban_House_Zone3_56', 41.705, 3.549, 9, 'Loading'],
['Factory_Zone3_57', 41.901, 3.8, 75, 'Unloading'], ['Office_Zone1_58', 40.75, -9.519, 96, 'Loading'], ['Farm_Zone3_59', 41.977, 3.778, 62, 'Unloading'],
['Repair_Center_Zone1_60', 40.557, '-9.347', 260, 'Loading'], ['Factory_Zone2_61', 45.44, 13.768, 3, 'Unloading'], ['High_Rise_Building_Zone3_62', 41.562, 3.468, 60, 'Loading'],
['Store_Zone3_63', 41.975, 3.178, 13, 'Unloading'], ['Post_Office_Zone3_64', '41.018', 3.323, 44, 'Loading'], ['Farm_Zone3_65', 41.397, '3.616', 81, 'Unloading'],
['Post_Office_Zone2_66', 44.393, 13.063, 51, 'Loading'], ['Office_Zone3_67', 41.343, 3.995, 89, 'Unloading'], ['Store_Zone3_68', 41.489, 3.746, 27, 'Loading'],
['Factory_Zone3_69', 41.242, 3.693, 47, 'Unloading'], ['Post_Office_Zone3_70', 41.283, '3.379', 102, 'Loading'], ['Office_Zone1_71', 40.719, -9.92, 4, 'Unloading'],
['Store_Zone3_72', 41.658, 3.162, 36, 'Loading'], ['Post_Office_Zone3_73', 41.912, 3.245, 83, 'Unloading'], ['Farm_Zone1_74', 40.416, -9.48, 45, 'Loading'],
['High_Rise_Building_Zone2_75', 45.093, '13.199', 16, 'Unloading'], ['Post_Office_Zone3_76', 41.559, 3.533, 45, 'Loading'], ['Post_Office_Zone2_77', 44.395, 13.812, 25, 'Unloading'],
['Suburban_House_Zone2_78', 45.375, 13.261, 43, 'Loading'], ['Post_Office_Zone3_79', 41.09, 3.504, 12, 'Unloading'], ['Suburban_House_Zone1_80', 40.811, '-9.976', 217, 'Loading'],
['Store_Zone2_81', 44.032, 13.82, 47, 'Unloading'], ['Depot_Zone2_82', 45.761, 13.426, 81, 'Loading'], ['Farm_Zone3_83', 41.817, 3.302, 59, 'Unloading'],
['Farm_Zone3_84', 41.928, 3.777, 11, 'Loading'], ['Repair_Center_Zone2_85', 44.55, '13.48', 70, 'Unloading'], ['Train_Station_Zone2_86', 45.396, 13.869, 46, 'Loading'],
['Office_Zone2_87', 45.649, 13.15, 1, 'Unloading'], ['Train_Station_Zone2_88', 44.628, 13.237, 80, 'Loading'], ['Suburban_House_Zone2_89', 45.79, 13.386, 52, 'Unloading'],
['Suburban_House_Zone3_90', 41.964, '3.462', 271, 'Loading'], ['Farm_Zone3_91', 41.356, 3.094, 65, 'Unloading'], ['Warehouse_Zone1_92', 40.266, -9.922, 72, 'Loading'],
['Repair_Center_Zone2_93', 45.603, 13.18, 74, 'Unloading'], ['Suburban_House_Zone3_94', 41.25, 3.669, 24, 'Loading'], ['Office_Zone3_95', 41.269, '3.278', 89, 'Unloading'],
['Farm_Zone1_96', '40.016', -9.902, 82, 'Loading'], ['Train_Station_Zone1_97', 40.47, -9.25, 16, 'Unloading'], ['Suburban_House_Zone2_98', 45.968, 13.031, 16, 'Loading'],
['Factory_Zone3_99', 41.905, 3.428, 0, 'Unloading'], ['Office_Zone3_100', 41.047, '3.634', 156, 'Loading'], ['High_Rise_Building_Zone2_101', 44.204, 13.295, 21, 'Unloading'],
['Office_Zone1_102', 40.16, -9.346, 77, 'Loading'], ['Factory_Zone2_103', 45.349, 13.235, 22, 'Unloading'], ['Warehouse_Zone1_104', 40.165, -9.139, 9, 'Loading'],
['Depot_Zone2_105', 45.119, '13.982', 45, 'Unloading'], ['Farm_Zone1_106', 40.338, -9.295, 95, 'Loading'], ['High_Rise_Building_Zone2_107', 45.987, 13.87, 17, 'Unloading'],
['High_Rise_Building_Zone1_108', 40.801, -9.517, 91, 'Loading'], ['High_Rise_Building_Zone1_109', 40.213, -9.707, 49, 'Unloading'], ['Store_Zone3_110', 41.316, '3.646', 209, 'Loading'],
['Depot_Zone2_111', 44.561, 13.358, 85, 'Unloading'], ['Suburban_House_Zone1_112', 40.099, -9.207, 30, 'Loading'], ['Store_Zone1_113', 40.512, -9.916, 71, 'Unloading'],
['Factory_Zone1_114', 40.214, -9.76, 56, 'Loading'], ['Post_Office_Zone2_115', 44.372, '13.203', 49, 'Unloading'], ['Warehouse_Zone1_116', 40.23, -9.82, 70, 'Loading'],
['Factory_Zone3_117', 41.286, 3.309, 74, 'Unloading'], ['Store_Zone1_118', 40.899, -9.179, 23, 'Loading'], ['High_Rise_Building_Zone2_119', 45.349, 13.177, 8, 'Unloading'],
['Store_Zone3_120', 41.667, '3.178', 173, 'Loading'], ['Warehouse_Zone1_121', 40.921, -9.151, 44, 'Unloading'], ['Warehouse_Zone3_122', 41.726, 3.073, 62, 'Loading'],
['Factory_Zone1_123', 40.989, -9.054, 48, 'Unloading'], ['Office_Zone3_124', 41.319, 3.664, 85, 'Loading'], ['Factory_Zone3_125', 41.402, '3.653', 27, 'Unloading'],
['Warehouse_Zone3_126', 41.918, 3.77, 65, 'Loading'], ['High_Rise_Building_Zone1_127', 40.101, -9.27, 48, 'Unloading'], ['Train_Station_Zone1_128', '40.288', -9.01, 1, 'Loading'],
['Farm_Zone1_129', 40.429, -9.667, 85, 'Unloading'], ['Farm_Zone2_130', 44.15, '13.967', 112, 'Loading'], ['Depot_Zone2_131', 44.575, 13.898, 12, 'Unloading'],
['Repair_Center_Zone3_132', 41.167, 3.177, 46, 'Loading'], ['Store_Zone3_133', 41.866, 3.852, 84, 'Unloading'], ['Store_Zone1_134', 40.995, -9.627, 11, 'Loading'],
['Train_Station_Zone1_135', 40.282, '-9.792', 59, 'Unloading'], ['Store_Zone2_136', 45.178, 13.742, 68, 'Loading'], ['Suburban_House_Zone3_137', 41.147, 3.533, 0, 'Unloading'],
['Post_Office_Zone2_138', 44.096, 13.388, 94, 'Loading'], ['High_Rise_Building_Zone2_139', 44.235, 13.224, 31, 'Unloading'], ['Farm_Zone3_140', 41.257, '3.691', 175, 'Loading'],
['Train_Station_Zone2_141', 45.716, 13.127, 46, 'Unloading'], ['Warehouse_Zone2_142', 44.096, 13.578, 60, 'Loading'], ['Post_Office_Zone2_143', 45.441, 13.706, 55, 'Unloading'],
['Suburban_House_Zone2_144', 45.235, 13.082, 60, 'Loading'], ['Farm_Zone3_145', 41.64, '3.93', 80, 'Unloading'], ['Depot_Zone2_146', 44.441, 13.753, 48, 'Loading'],
['Store_Zone3_147', 41.532, 3.211, 78, 'Unloading'], ['High_Rise_Building_Zone3_148', 41.926, 3.099, 3, 'Loading'], ['Suburban_House_Zone2_149', 45.309, 13.086, 29, 'Unloading'],
['Suburban_House_Zone1_150', 40.595, '-9.737', 209, 'Loading'], ['High_Rise_Building_Zone2_151', 45.842, 13.542, 57, 'Unloading'], ['Warehouse_Zone1_152', 40.525, -9.37, 89, 'Loading'],
['Warehouse_Zone2_153', 45.179, 13.478, 82, 'Unloading'], ['Post_Office_Zone2_154', 44.921, 13.03, 11, 'Loading'], ['Depot_Zone2_155', 44.4, '13.822', 12, 'Unloading'],
['Suburban_House_Zone2_156', 45.599, 13.883, 57, 'Loading'], ['Train_Station_Zone3_157', 41.628, 3.232, 46, 'Unloading'], ['Repair_Center_Zone2_158', 45.067, 13.339, 32, 'Loading'],
['Post_Office_Zone3_159', 41.698, 3.85, 30, 'Unloading'], ['Farm_Zone3_160', '41.969', '3.488', 181, 'Loading'], ['Store_Zone2_161', 45.127, 13.672, 77, 'Unloading'],
['Store_Zone1_162', 40.193, -9.637, 82, 'Loading'], ['Train_Station_Zone3_163', 41.931, 3.267, 75, 'Unloading'], ['Warehouse_Zone2_164', 45.311, 13.32, 72, 'Loading'],
['Post_Office_Zone1_165', 40.386, '-9.482', 86, 'Unloading'], ['Depot_Zone1_166', 40.307, -9.646, 34, 'Loading'], ['Office_Zone1_167', 40.704, -9.221, 71, 'Unloading'],
['Store_Zone2_168', 45.859, 13.548, 80, 'Loading'], ['Warehouse_Zone2_169', 44.335, 13.106, 65, 'Unloading'], ['Train_Station_Zone3_170', 41.183, '3.843', 242, 'Loading'],
['High_Rise_Building_Zone2_171', 44.2, 13.705, 51, 'Unloading'], ['Warehouse_Zone3_172', 41.474, 3.645, 14, 'Loading'], ['Store_Zone1_173', 40.1, -9.086, 24, 'Unloading'],
['Warehouse_Zone2_174', 45.569, 13.051, 84, 'Loading'], ['Office_Zone3_175', 41.634, '3.279', 71, 'Unloading'], ['Office_Zone3_176', 41.199, 3.016, 19, 'Loading'],
['High_Rise_Building_Zone1_177', 40.321, -9.663, 49, 'Unloading'], ['Office_Zone2_178', 44.909, 13.187, 0, 'Loading'], ['Repair_Center_Zone3_179', 41.574, 3.238, 28, 'Unloading'],
['Warehouse_Zone3_180', 41.983, '3.078', 148, 'Loading'], ['Office_Zone1_181', 40.908, -9.129, 48, 'Unloading'], ['Warehouse_Zone2_182', 44.607, 13.313, 89, 'Loading'],
['Factory_Zone3_183', 41.876, 3.47, 87, 'Unloading'], ['Farm_Zone2_184', 44.657, 13.612, 85, 'Loading'], ['Factory_Zone2_185', 45.054, '13.934', 49, 'Unloading'],
['Office_Zone1_186', 40.338, -9.057, 16, 'Loading'], ['Suburban_House_Zone1_187', 40.481, -9.452, 60, 'Unloading'], ['Train_Station_Zone3_188', 41.95, 3.543, 95, 'Loading'],
['Depot_Zone1_189', 40.423, -9.091, 39, 'Unloading'], ['Warehouse_Zone3_190', 41.093, '3.829', 258, 'Loading'], ['High_Rise_Building_Zone3_191', 41.673, 3.735, 61, 'Unloading'],
['Post_Office_Zone3_192', '41.348', 3.977, 25, 'Loading'], ['Repair_Center_Zone3_193', 41.985, 3.469, 45, 'Unloading'], ['Factory_Zone2_194', 44.993, 13.645, 59, 'Loading'],
['Suburban_House_Zone1_195', 40.107, '-9.377', 51, 'Unloading'], ['Post_Office_Zone1_196', 40.834, -9.978, 49, 'Loading'], ['Farm_Zone2_197', 45.604, 13.03, 52, 'Unloading'],
['Office_Zone1_198', 40.755, -9.306, 78, 'Loading'], ['Office_Zone3_199', 41.429, 3.2, 45, 'Unloading'], ['Post_Office_Zone2_200', 44.517, '13.312', 127, 'Loading'],
['High_Rise_Building_Zone2_201', 44.737, 13.371, 30, 'Unloading'], ['Train_Station_Zone2_202', 45.821, 13.815, 17, 'Loading'], ['High_Rise_Building_Zone1_203', 40.971, -9.68, 56, 'Unloading'],
['Factory_Zone3_204', 41.568, 3.059, 29, 'Loading'], ['Office_Zone1_205', 40.529, '-9.969', 14, 'Unloading'], ['High_Rise_Building_Zone2_206', 45.802, 13.727, 78, 'Loading'],
['Factory_Zone2_207', 44.754, 13.345, 16, 'Unloading'], ['Office_Zone2_208', 44.408, 13.557, 51, 'Loading'], ['Store_Zone3_209', 41.298, 3.872, 96, 'Unloading'],
['Factory_Zone2_210', 44.639, '13.055', 284, 'Loading'], ['Depot_Zone1_211', 40.459, -9.578, 20, 'Unloading'], ['Train_Station_Zone2_212', 44.247, 13.005, 24, 'Loading'],
['Farm_Zone1_213', 40.668, -9.639, 77, 'Unloading'], ['Repair_Center_Zone3_214', 41.518, 3.356, 45, 'Loading'], ['Depot_Zone3_215', 41.312, '3.394', 26, 'Unloading'],
['Post_Office_Zone3_216', 41.91, 3.587, 87, 'Loading'], ['Repair_Center_Zone1_217', 40.876, -9.696, 77, 'Unloading'], ['Factory_Zone1_218', 40.192, -9.525, 21, 'Loading'],
['Train_Station_Zone2_219', 44.291, 13.303, 47, 'Unloading'], ['Farm_Zone3_220', 41.797, '3.799', 261, 'Loading'], ['High_Rise_Building_Zone1_221', 40.69, -9.541, 26, 'Unloading'],
['Post_Office_Zone1_222', 40.115, -9.337, 20, 'Loading'], ['Train_Station_Zone3_223', 41.661, 3.655, 35, 'Unloading'], ['High_Rise_Building_Zone1_224', '40.265', -9.914, 12, 'Loading'],
['High_Rise_Building_Zone1_225', 40.13, '-9.594', 65, 'Unloading'], ['Warehouse_Zone1_226', 40.221, -9.703, 18, 'Loading'], ['Repair_Center_Zone1_227', 40.923, -9.353, 73, 'Unloading'],
['Warehouse_Zone1_228', 40.166, -9.98, 17, 'Loading'], ['Store_Zone2_229', 45.541, 13.011, 16, 'Unloading'], ['Post_Office_Zone1_230', 40.039, '-9.044', 185, 'Loading'],
['Warehouse_Zone3_231', 41.221, 3.132, 59, 'Unloading'], ['Factory_Zone2_232', 45.461, 13.708, 0, 'Loading'], ['Post_Office_Zone3_233', 41.403, 3.809, 36, 'Unloading'],
['Depot_Zone3_234', 41.048, 3.698, 51, 'Loading'], ['Warehouse_Zone2_235', 45.721, '13.691', 47, 'Unloading'], ['Train_Station_Zone2_236', 44.025, 13.729, 45, 'Loading'],
['High_Rise_Building_Zone1_237', 40.431, -9.773, 81, 'Unloading'], ['Post_Office_Zone2_238', 45.355, 13.001, 64, 'Loading'], ['Warehouse_Zone3_239', 41.197, 3.41, 61, 'Unloading'],
['Store_Zone1_240', 40.722, '-9.346', 243, 'Loading'], ['Farm_Zone3_241', 41.469, 3.644, 55, 'Unloading'], ['Depot_Zone1_242', 40.95, -9.257, 19, 'Loading'],
['Farm_Zone1_243', 40.816, -9.374, 48, 'Unloading'], ['Depot_Zone2_244', 44.501, 13.296, 95, 'Loading'], ['Depot_Zone1_245', 40.624, '-9.076', 55, 'Unloading'],
['High_Rise_Building_Zone3_246', 41.513, 3.54, 12, 'Loading'], ['Office_Zone1_247', 40.626, -9.066, 65, 'Unloading'], ['Post_Office_Zone2_248', 44.127, 13.323, 0, 'Loading'],
['Repair_Center_Zone3_249', 41.773, 3.595, 21, 'Unloading'], ['Repair_Center_Zone1_250', 40.966, '-9.348', 171, 'Loading'], ['Farm_Zone1_251', 40.682, -9.117, 92, 'Unloading'],
['Store_Zone2_252', 44.309, 13.952, 99, 'Loading'], ['High_Rise_Building_Zone2_253', 45.37, 13.813, 39, 'Unloading'], ['Repair_Center_Zone3_254', 41.502, 3.739, 91, 'Loading'],
['Post_Office_Zone3_255', 41.758, '3.117', 76, 'Unloading'], ['Farm_Zone1_256', '40.679', -9.426, 86, 'Loading'], ['Factory_Zone2_257', 45.104, 13.564, 89, 'Unloading'],
['Farm_Zone2_258', 44.993, 13.862, 38, 'Loading'], ['Farm_Zone2_259', 45.887, 13.188, 23, 'Unloading'], ['Warehouse_Zone3_260', 41.323, '3.441', 272, 'Loading'],
['Farm_Zone1_261', 40.151, -9.085, 74, 'Unloading'], ['Store_Zone1_262', 40.09, -9.489, 26, 'Loading'], ['Suburban_House_Zone1_263', 40.688, -9.465, 81, 'Unloading'],
['Suburban_House_Zone3_264', 41.516, 3.675, 19, 'Loading'], ['High_Rise_Building_Zone2_265', 44.048, '13.658', 38, 'Unloading'], ['Depot_Zone1_266', 40.454, -9.137, 27, 'Loading'],
['High_Rise_Building_Zone2_267', 45.605, 13.234, 74, 'Unloading'], ['Post_Office_Zone1_268', 40.497, -9.003, 53, 'Loading'], ['High_Rise_Building_Zone3_269', 41.632, 3.027, 62, 'Unloading'],
['Post_Office_Zone3_270', 41.465, '3.324', 265, 'Loading'], ['High_Rise_Building_Zone1_271', 40.015, -9.108, 20, 'Unloading'], ['High_Rise_Building_Zone3_272', 41.25, 3.074, 26, 'Loading'],
['Train_Station_Zone2_273', 44.85, 13.047, 91, 'Unloading'], ['Store_Zone3_274', 41.333, 3.907, 60, 'Loading'], ['Warehouse_Zone3_275', 41.287, '3.456', 90, 'Unloading'],
['Repair_Center_Zone3_276', 41.629, 3.879, 25, 'Loading'], ['Repair_Center_Zone3_277', 41.98, 3.29, 73, 'Unloading'], ['Factory_Zone2_278', 45.141, 13.928, 45, 'Loading'],
['Office_Zone2_279', 45.107, 13.271, 20, 'Unloading'], ['Warehouse_Zone1_280', 40.648, '-9.298', 200, 'Loading'], ['Office_Zone1_281', 40.99, -9.669, 21, 'Unloading'],
['Store_Zone2_282', 44.707, 13.934, 36, 'Loading'], ['Suburban_House_Zone3_283', 41.464, 3.222, 4, 'Unloading'], ['Office_Zone1_284', 40.94, -9.755, 93, 'Loading'],
['Train_Station_Zone1_285', 40.557, '-9.516', 37, 'Unloading'], ['Repair_Center_Zone1_286', 40.562, -9.236, 26, 'Loading'], ['Farm_Zone3_287', 41.953, 3.264, 1, 'Unloading'],
['Warehouse_Zone1_288', '40.672', -9.568, 99, 'Loading'], ['Depot_Zone1_289', 40.949, -9.624, 6, 'Unloading'], ['High_Rise_Building_Zone2_290', 44.446, '13.287', 215, 'Loading'],
['Post_Office_Zone2_291', 45.396, 13.398, 19, 'Unloading'], ['Depot_Zone2_292', 45.292, 13.582, 12, 'Loading'], ['Train_Station_Zone3_293', 41.01, 3.278, 23, 'Unloading'],
['Train_Station_Zone1_294', 40.183, -9.113, 70, 'Loading'], ['High_Rise_Building_Zone2_295', 45.979, '13.347', 41, 'Unloading'], ['Farm_Zone3_296', 41.224, 3.411, 10, 'Loading'],
['Office_Zone2_297', 45.683, 13.83, 61, 'Unloading'], ['Train_Station_Zone1_298', 40.874, -9.716, 17, 'Loading'], ['Post_Office_Zone1_299', 40.536, -9.04, 39, 'Unloading'],
['Train_Station_Zone1_300', 40.718, '-9.232', 294, 'Loading'], ['Warehouse_Zone2_301', 44.837, 13.683, 63, 'Unloading'], ['Warehouse_Zone1_302', 40.332, -9.556, 95, 'Loading'],
['Post_Office_Zone3_303', 41.389, 3.669, 54, 'Unloading'], ['High_Rise_Building_Zone1_304', 40.886, -9.136, 31, 'Loading'], ['Warehouse_Zone1_305', 40.316, '-9.078', 91, 'Unloading'],
['Post_Office_Zone2_306', 45.16, 13.27, 37, 'Loading'], ['Store_Zone1_307', 40.673, -9.226, 73, 'Unloading'], ['Factory_Zone1_308', 40.801, -9.079, 85, 'Loading'],
['Office_Zone3_309', 41.903, 3.039, 74, 'Unloading'], ['Repair_Center_Zone3_310', 41.344, '3.548', 112, 'Loading'], ['Train_Station_Zone3_311', 41.795, 3.768, 52, 'Unloading'],
['Post_Office_Zone2_312', 45.17, 13.986, 17, 'Loading'], ['Suburban_House_Zone3_313', 41.36, 3.28, 97, 'Unloading'], ['Post_Office_Zone2_314', 45.562, 13.471, 26, 'Loading'],
['Suburban_House_Zone2_315', 45.142, '13.243', 67, 'Unloading'], ['Train_Station_Zone3_316', 41.22, 3.322, 48, 'Loading'], ['Train_Station_Zone1_317', 40.748, -9.043, 56, 'Unloading'],
['Post_Office_Zone2_318', 45.511, 13.31, 36, 'Loading'], ['Train_Station_Zone1_319', 40.704, -9.634, 96, 'Unloading'], ['Train_Station_Zone1_320', '40.325', '-9.036', 117, 'Loading'],
['Warehouse_Zone1_321', 40.103, -9.746, 81, 'Unloading'], ['Suburban_House_Zone1_322', 40.192, -9.44, 81, 'Loading'], ['High_Rise_Building_Zone1_323', 40.833, -9.041, 5, 'Unloading'],
['Train_Station_Zone3_324', 41.419, 3.091, 37, 'Loading'], ['Depot_Zone1_325', 40.199, '-9.922', 74, 'Unloading'], ['High_Rise_Building_Zone3_326', 41.896, 3.493, 42, 'Loading'],
['High_Rise_Building_Zone3_327', 41.599, 3.28, 98, 'Unloading'], ['Office_Zone2_328', 45.755, 13.846, 12, 'Loading'], ['Depot_Zone3_329', 41.308, 3.654, 50, 'Unloading'],
['Post_Office_Zone2_330', 45.251, '13.771', 192, 'Loading'], ['Office_Zone1_331', 40.373, -9.123, 67, 'Unloading'], ['Post_Office_Zone1_332', 40.938, -9.524, 54, 'Loading'],
['Store_Zone2_333', 44.035, 13.772, 71, 'Unloading'], ['Post_Office_Zone3_334', 41.842, 3.345, 18, 'Loading'], ['Farm_Zone3_335', 41.368, '3.812', 83, 'Unloading'],
['Store_Zone3_336', 41.054, 3.144, 16, 'Loading'], ['Suburban_House_Zone2_337', 45.479, 13.013, 47, 'Unloading'], ['Depot_Zone2_338', 44.59, 13.509, 15, 'Loading'],
['Office_Zone1_339', 40.91, -9.203, 9, 'Unloading'], ['Office_Zone2_340', 44.963, '13.517', 133, 'Loading'], ['Suburban_House_Zone2_341', 44.025, 13.714, 27, 'Unloading'],
['Factory_Zone3_342', 41.364, 3.739, 60, 'Loading'], ['Store_Zone1_343', 40.229, -9.334, 36, 'Unloading'], ['Farm_Zone2_344', 45.756, 13.268, 22, 'Loading'],
['Factory_Zone1_345', 40.067, '-9.589', 39, 'Unloading'], ['Office_Zone1_346', 40.507, -9.941, 19, 'Loading'], ['Store_Zone3_347', 41.048, 3.912, 96, 'Unloading'],
['Farm_Zone3_348', 41.882, 3.124, 75, 'Loading'], ['Warehouse_Zone1_349', 40.255, -9.263, 13, 'Unloading'], ['Suburban_House_Zone3_350', 41.351, '3.014', 248, 'Loading'],
['Factory_Zone3_351', 41.504, 3.131, 19, 'Unloading'], ['Farm_Zone2_352', '44.333', 13.611, 44, 'Loading'], ['Store_Zone2_353', 45.105, 13.077, 77, 'Unloading'],
['Office_Zone2_354', 44.91, 13.987, 84, 'Loading'], ['Suburban_House_Zone3_355', 41.874, '3.632', 89, 'Unloading'], ['Train_Station_Zone3_356', 41.095, 3.846, 49, 'Loading'],
['Factory_Zone3_357', 41.345, 3.133, 43, 'Unloading'], ['Depot_Zone2_358', 45.165, 13.273, 51, 'Loading'], ['Repair_Center_Zone1_359', 40.131, -9.519, 0, 'Unloading'],
['Office_Zone3_360', 41.35, '3.427', 143, 'Loading'], ['Train_Station_Zone2_361', 44.678, 13.824, 84, 'Unloading'], ['Farm_Zone1_362', 40.707, -9.613, 78, 'Loading'],
['Depot_Zone3_363', 41.753, 3.521, 44, 'Unloading'], ['High_Rise_Building_Zone1_364', 40.344, -9.721, 15, 'Loading'], ['Train_Station_Zone2_365', 45.19, '13.089', 68, 'Unloading'],
['Repair_Center_Zone3_366', 41.177, 3.678, 32, 'Loading'], ['Repair_Center_Zone3_367', 41.883, 3.756, 83, 'Unloading'], ['Suburban_House_Zone2_368', 44.035, 13.982, 71, 'Loading'],
['High_Rise_Building_Zone3_369', 41.593, 3.113, 89, 'Unloading'], ['Repair_Center_Zone3_370', 41.071, '3.081', 125, 'Loading'], ['Post_Office_Zone1_371', 40.107, -9.223, 95, 'Unloading'],
['Depot_Zone2_372', 45.521, 13.877, 100, 'Loading'], ['Office_Zone2_373', 45.677, 13.104, 16, 'Unloading'], ['Store_Zone2_374', 44.713, 13.803, 53, 'Loading'],
['Farm_Zone2_375', 44.013, '13.312', 1, 'Unloading'], ['High_Rise_Building_Zone1_376', 40.174, -9.571, 44, 'Loading'], ['Warehouse_Zone3_377', 41.819, 3.763, 92, 'Unloading'],
['Farm_Zone2_378', 45.866, 13.698, 69, 'Loading'], ['Warehouse_Zone3_379', 41.051, 3.821, 2, 'Unloading'], ['Post_Office_Zone2_380', 45.664, '13.335', 212, 'Loading'],
['Repair_Center_Zone1_381', 40.158, -9.161, 15, 'Unloading'], ['Suburban_House_Zone2_382', 45.903, 13.982, 70, 'Loading'], ['High_Rise_Building_Zone2_383', 44.49, 13.005, 61, 'Unloading'],
['Store_Zone2_384', '44.824', 13.713, 92, 'Loading'], ['Post_Office_Zone3_385', 41.305, '3.255', 33, 'Unloading'], ['Warehouse_Zone2_386', 45.364, 13.778, 43, 'Loading'],
['Farm_Zone3_387', 41.853, 3.58, 84, 'Unloading'], ['Repair_Center_Zone2_388', 44.515, 13.13, 86, 'Loading'], ['High_Rise_Building_Zone1_389', 40.86, -9.693, 57, 'Unloading'],
['Factory_Zone2_390', 44.93, '13.064', 164, 'Loading'], ['Factory_Zone2_391', 45.578, 13.337, 20, 'Unloading'], ['Store_Zone3_392', 41.743, 3.678, 23, 'Loading'],
['Post_Office_Zone3_393', 41.078, 3.816, 61, 'Unloading'], ['Farm_Zone1_394', 40.695, -9.255, 12, 'Loading'], ['Farm_Zone3_395', 41.29, '3.397', 80, 'Unloading'],
['Suburban_House_Zone2_396', 45.584, 13.007, 74, 'Loading'], ['Store_Zone2_397', 44.699, 13.399, 96, 'Unloading'], ['Depot_Zone1_398', 40.439, -9.976, 12, 'Loading'],
['High_Rise_Building_Zone2_399', 44.687, 13.494, 39, 'Unloading'], ['Office_Zone1_400', 40.386, '-9.941', 121, 'Loading'], ['Farm_Zone1_401', 40.144, -9.426, 6, 'Unloading'],
['High_Rise_Building_Zone2_402', 44.431, 13.445, 52, 'Loading'], ['Repair_Center_Zone3_403', 41.95, 3.427, 25, 'Unloading'], ['Suburban_House_Zone1_404', 40.749, -9.788, 55, 'Loading'],
['Repair_Center_Zone1_405', 40.645, '-9.755', 97, 'Unloading'], ['Post_Office_Zone1_406', 40.561, -9.911, 72, 'Loading'], ['Store_Zone3_407', 41.23, 3.052, 91, 'Unloading'],
['Suburban_House_Zone3_408', 41.614, 3.86, 28, 'Loading'], ['Suburban_House_Zone1_409', 40.79, -9.033, 81, 'Unloading'], ['Train_Station_Zone3_410', 41.164, '3.692', 244, 'Loading'],
['Factory_Zone3_411', 41.539, 3.405, 80, 'Unloading'], ['Train_Station_Zone3_412', 41.734, 3.469, 59, 'Loading'], ['Repair_Center_Zone2_413', 45.33, 13.977, 93, 'Unloading'],
['Office_Zone1_414', 40.391, -9.34, 49, 'Loading'], ['Train_Station_Zone2_415', 44.65, '13.159', 37, 'Unloading'], ['Warehouse_Zone3_416', '41.504', 3.932, 89, 'Loading'],
['Repair_Center_Zone3_417', 41.847, 3.327, 71, 'Unloading'], ['High_Rise_Building_Zone2_418', 44.117, 13.862, 8, 'Loading'], ['Train_Station_Zone3_419', 41.097, 3.047, 2, 'Unloading'],
['Warehouse_Zone3_420', 41.466, '3.537', 254, 'Loading'], ['Store_Zone2_421', 44.055, 13.037, 11, 'Unloading'], ['Office_Zone3_422', 41.012, 3.807, 27, 'Loading'],
['Farm_Zone2_423', 45.328, 13.788, 72, 'Unloading'], ['Suburban_House_Zone1_424', 40.472, -9.216, 89, 'Loading'], ['Farm_Zone1_425', 40.94, '-9.156', 32, 'Unloading'],
['Suburban_House_Zone2_426', 45.719, 13.793, 78, 'Loading'], ['Depot_Zone3_427', 41.651, 3.766, 69, 'Unloading'], ['Suburban_House_Zone3_428', 41.168, 3.026, 47, 'Loading'],
['Repair_Center_Zone2_429', 45.162, 13.992, 92, 'Unloading'], ['Post_Office_Zone3_430', 41.755, '3.324', 213, 'Loading'], ['Train_Station_Zone1_431', 40.29, -9.127, 49, 'Unloading'],
['Post_Office_Zone1_432', 40.018, -9.749, 93, 'Loading'], ['Post_Office_Zone3_433', 41.674, 3.208, 56, 'Unloading'], ['Suburban_House_Zone1_434', 40.159, -9.804, 96, 'Loading'],
['Train_Station_Zone2_435', 45.222, '13.889', 33, 'Unloading'], ['Warehouse_Zone3_436', 41.153, 3.352, 88, 'Loading'], ['Post_Office_Zone1_437', 40.727, -9.564, 12, 'Unloading'],
['Warehouse_Zone3_438', 41.972, 3.638, 36, 'Loading'], ['Factory_Zone1_439', 40.499, -9.596, 42, 'Unloading'], ['Suburban_House_Zone2_440', 45.305, '13.94', 158, 'Loading'],
['Repair_Center_Zone2_441', 44.099, 13.387, 19, 'Unloading'], ['Repair_Center_Zone3_442', 41.423, 3.469, 31, 'Loading'], ['Factory_Zone3_443', 41.256, 3.186, 74, 'Unloading'],
['High_Rise_Building_Zone3_444', 41.128, 3.051, 93, 'Loading'], ['Factory_Zone1_445', 40.42, '-9.882', 89, 'Unloading'], ['Train_Station_Zone1_446', 40.134, -9.677, 99, 'Loading'],
['Office_Zone1_447', 40.415, -9.331, 93, 'Unloading'], ['Warehouse_Zone2_448', '45.961', 13.643, 60, 'Loading'], ['Farm_Zone3_449', 41.844, 3.756, 92, 'Unloading'],
['Suburban_House_Zone1_450', 40.188, '-9.739', 219, 'Loading'], ['Warehouse_Zone1_451', 40.533, -9.121, 100, 'Unloading'], ['Farm_Zone1_452', 40.309, -9.331, 0, 'Loading'],
['Depot_Zone3_453', 41.641, 3.204, 47, 'Unloading'], ['Depot_Zone1_454', 40.351, -9.495, 83, 'Loading'], ['Suburban_House_Zone3_455', 41.591, '3.596', 18, 'Unloading'],
['Factory_Zone2_456', 44.404, 13.98, 56, 'Loading'], ['Depot_Zone1_457', 40.66, -9.755, 55, 'Unloading'], ['Depot_Zone2_458', 45.586, 13.287, 4, 'Loading'],
['Factory_Zone1_459', 40.853, -9.571, 65, 'Unloading'], ['Depot_Zone3_460', 41.601, '3.429', 122, 'Loading'], ['Post_Office_Zone3_461', 41.475, 3.772, 68, 'Unloading'],
['Repair_Center_Zone2_462', 45.096, 13.099, 41, 'Loading'], ['Office_Zone1_463', 40.516, -9.572, 18, 'Unloading'], ['Factory_Zone3_464', 41.396, 3.756, 59, 'Loading'],
['Warehouse_Zone2_465', 44.798, '13.405', 38, 'Unloading'], ['Warehouse_Zone3_466', 41.353, 3.902, 83, 'Loading'], ['Repair_Center_Zone1_467', 40.92, -9.828, 82, 'Unloading'],
['Farm_Zone3_468', 41.46, 3.759, 63, 'Loading'], ['Store_Zone1_469', 40.311, -9.925, 50, 'Unloading'], ['Repair_Center_Zone1_470', 40.341, '-9.047', 203, 'Loading'],
['Warehouse_Zone3_471', 41.152, 3.143, 38, 'Unloading'], ['Repair_Center_Zone2_472', 44.015, 13.425, 17, 'Loading'], ['High_Rise_Building_Zone3_473', 41.326, 3.455, 94, 'Unloading'],
['Depot_Zone1_474', 40.817, -9.413, 28, 'Loading'], ['Suburban_House_Zone2_475', 45.017, '13.018', 17, 'Unloading'], ['Post_Office_Zone2_476', 44.364, 13.346, 63, 'Loading'],
['Warehouse_Zone2_477', 44.662, 13.636, 64, 'Unloading'], ['Factory_Zone3_478', 41.064, 3.024, 94, 'Loading'], ['Office_Zone2_479', 45.107, 13.676, 17, 'Unloading'],
['Repair_Center_Zone1_480', '40.687', '-9.328', 101, 'Loading'], ['High_Rise_Building_Zone3_481', 41.94, 3.06, 93, 'Unloading'], ['Post_Office_Zone3_482', 41.707, 3.86, 1, 'Loading'],
['Train_Station_Zone1_483', 40.668, -9.773, 41, 'Unloading'], ['Factory_Zone3_484', 41.796, 3.322, 15, 'Loading'], ['Office_Zone1_485', 40.463, '-9.679', 15, 'Unloading'],
['Depot_Zone3_486', 41.61, 3.538, 82, 'Loading'], ['Warehouse_Zone2_487', 45.574, 13.699, 77, 'Unloading'], ['Store_Zone2_488', 45.564, 13.399, 95, 'Loading'],
['Farm_Zone1_489', 40.771, -9.981, 4, 'Unloading'], ['Farm_Zone2_490', 44.949, '13.737', 243, 'Loading'], ['Warehouse_Zone2_491', 45.889, 13.792, 7, 'Unloading'],
['Store_Zone1_492', 40.706, -9.806, 67, 'Loading'], ['High_Rise_Building_Zone3_493', 41.157, 3.493, 70, 'Unloading'], ['Factory_Zone3_494', 41.666, 3.785, 85, 'Loading'],
['High_Rise_Building_Zone3_495', 41.823, '3.815', 40, 'Unloading'], ['Depot_Zone3_496', 41.458, 3.903, 78, 'Loading'], ['Warehouse_Zone2_497', 44.488, 13.006, 70, 'Unloading'],
['Depot_Zone3_498', 41.787, 3.328, 84, 'Loading'], ['Train_Station_Zone1_499', 40.152, -9.52, 93, 'Unloading'], ['Repair_Center_Zone2_500', 44.129, '13.595', 278, 'Loading'],
['Office_Zone1_501', 40.808, -9.033, 58, 'Unloading'], ['Train_Station_Zone2_502', 45.913, 13.959, 9, 'Loading'], ['Train_Station_Zone1_503', 40.041, -9.722, 50, 'Unloading'],
['High_Rise_Building_Zone2_504', 44.385, 13.843, 23, 'Loading'], ['Depot_Zone1_505', 40.776, '-9.043', 11, 'Unloading'], ['Suburban_House_Zone2_506', 45.601, 13.316, 34, 'Loading'],
['Farm_Zone1_507', 40.053, -9.413, 92, 'Unloading'], ['Office_Zone1_508', 40.623, -9.421, 94, 'Loading'], ['Repair_Center_Zone2_509', 44.148, 13.369, 24, 'Unloading'],
['Depot_Zone2_510', 45.663, '13.811', 297, 'Loading'], ['Office_Zone2_511', 44.8, 13.199, 21, 'Unloading'], ['Post_Office_Zone2_512', '44.329', 13.984, 81, 'Loading'],
['Factory_Zone3_513', 41.198, 3.214, 55, 'Unloading'], ['High_Rise_Building_Zone3_514', 41.974, 3.222, 91, 'Loading'], ['Suburban_House_Zone3_515', 41.897, '3.337', 26, 'Unloading'],
['Store_Zone3_516', 41.363, 3.585, 21, 'Loading'], ['Warehouse_Zone2_517', 45.213, 13.764, 55, 'Unloading'], ['Repair_Center_Zone1_518', 40.115, -9.24, 54, 'Loading'],
['Farm_Zone3_519', 41.823, 3.589, 74, 'Unloading'], ['Depot_Zone3_520', 41.056, '3.315', 208, 'Loading'], ['Suburban_House_Zone3_521', 41.882, 3.819, 74, 'Unloading'],
['Store_Zone2_522', 45.696, 13.768, 63, 'Loading'], ['Repair_Center_Zone1_523', 40.886, -9.973, 32, 'Unloading'], ['Depot_Zone3_524', 41.245, 3.649, 38, 'Loading'],
['High_Rise_Building_Zone2_525', 44.79, '13.896', 36, 'Unloading'], ['Store_Zone1_526', 40.422, -9.449, 73, 'Loading'], ['Post_Office_Zone1_527', 40.274, -9.73, 15, 'Unloading'],
['Farm_Zone2_528', 45.505, 13.961, 67, 'Loading'], ['Factory_Zone1_529', 40.163, -9.025, 42, 'Unloading'], ['Factory_Zone2_530', 45.181, '13.5', 189, 'Loading'],
['Repair_Center_Zone3_531', 41.064, 3.194, 45, 'Unloading'], ['Store_Zone1_532', 40.703, -9.198, 74, 'Loading'], ['Depot_Zone1_533', 40.503, -9.655, 51, 'Unloading'],
['Suburban_House_Zone2_534', 44.605, 13.781, 69, 'Loading'], ['Office_Zone1_535', 40.24, '-9.747', 99, 'Unloading'], ['Office_Zone1_536', 40.926, -9.428, 79, 'Loading'],
['Office_Zone1_537', 40.307, -9.905, 8, 'Unloading'], ['Store_Zone1_538', 40.326, -9.892, 37, 'Loading'], ['Office_Zone2_539', 45.123, 13.164, 17, 'Unloading'],
['Store_Zone1_540', 40.755, '-9.839', 291, 'Loading'], ['Depot_Zone2_541', 45.266, 13.283, 1, 'Unloading'], ['Post_Office_Zone1_542', 40.912, -9.261, 5, 'Loading'],
['Farm_Zone3_543', 41.673, 3.944, 52, 'Unloading'], ['Factory_Zone3_544', '41.03', 3.408, 42, 'Loading'], ['Train_Station_Zone3_545', 41.938, '3.308', 73, 'Unloading'],
['High_Rise_Building_Zone2_546', 45.374, 13.948, 84, 'Loading'], ['Store_Zone3_547', 41.64, 3.317, 96, 'Unloading'], ['High_Rise_Building_Zone2_548', 44.082, 13.127, 7, 'Loading'],
['Post_Office_Zone2_549', 45.139, 13.102, 8, 'Unloading'], ['Warehouse_Zone3_550', 41.037, '3.947', 274, 'Loading'], ['Train_Station_Zone2_551', 45.61, 13.163, 29, 'Unloading'],
['Post_Office_Zone2_552', 45.438, 13.149, 2, 'Loading'], ['Factory_Zone2_553', 45.245, 13.288, 4, 'Unloading'], ['Post_Office_Zone2_554', 44.257, 13.721, 51, 'Loading'],
['Factory_Zone3_555', 41.322, '3.089', 75, 'Unloading'], ['Farm_Zone3_556', 41.972, 3.262, 26, 'Loading'], ['Farm_Zone1_557', 40.157, -9.275, 88, 'Unloading'],
['High_Rise_Building_Zone1_558', 40.708, -9.869, 42, 'Loading'], ['Store_Zone2_559', 44.896, 13.907, 28, 'Unloading'], ['High_Rise_Building_Zone1_560', 40.565, '-9.969', 229, 'Loading'],
['Suburban_House_Zone1_561', 40.512, -9.344, 86, 'Unloading'], ['Post_Office_Zone2_562', 44.212, 13.946, 29, 'Loading'], ['Office_Zone2_563', 45.452, 13.723, 15, 'Unloading'],
['Post_Office_Zone1_564', 40.55, -9.133, 14, 'Loading'], ['Train_Station_Zone3_565', 41.385, '3.549', 76, 'Unloading'], ['Farm_Zone2_566', 44.836, 13.395, 22, 'Loading'],
['Post_Office_Zone3_567', 41.628, 3.628, 82, 'Unloading'], ['Depot_Zone3_568', 41.278, 3.759, 13, 'Loading'], ['Factory_Zone3_569', 41.429, 3.709, 86, 'Unloading'],
['Suburban_House_Zone3_570', 41.191, '3.411', 136, 'Loading'], ['Suburban_House_Zone1_571', 40.175, -9.761, 60, 'Unloading'], ['Post_Office_Zone2_572', 44.456, 13.665, 36, 'Loading'],
['Train_Station_Zone3_573', 41.164, 3.474, 99, 'Unloading'], ['Train_Station_Zone1_574', 40.86, -9.182, 77, 'Loading'], ['Store_Zone1_575', 40.459, '-9.481', 38, 'Unloading'],
['High_Rise_Building_Zone2_576', '45.196', 13.596, 12, 'Loading'], ['Farm_Zone1_577', 40.17, -9.444, 14, 'Unloading'], ['Farm_Zone2_578', 45.165, 13.125, 7, 'Loading'],
['Office_Zone3_579', 41.638, 3.504, 83, 'Unloading'], ['Office_Zone3_580', 41.744, '3.972', 182, 'Loading'], ['Factory_Zone1_581', 40.887, -9.959, 34, 'Unloading'],
['Office_Zone2_582', 44.136, 13.473, 13, 'Loading'], ['Store_Zone1_583', 40.958, -9.455, 25, 'Unloading'], ['Store_Zone2_584', 44.628, 13.61, 55, 'Loading'],
['Store_Zone1_585', 40.356, '-9.485', 43, 'Unloading'], ['Warehouse_Zone3_586', 41.495, 3.887, 33, 'Loading'], ['Farm_Zone3_587', 41.255, 3.647, 0, 'Unloading'],
['Post_Office_Zone1_588', 40.622, -9.184, 77, 'Loading'], ['Post_Office_Zone3_589', 41.932, 3.804, 40, 'Unloading'], ['Warehouse_Zone1_590', 40.006, '-9.104', 195, 'Loading'],
['Factory_Zone1_591', 40.887, -9.542, 39, 'Unloading'], ['Farm_Zone2_592', 45.207, 13.434, 55, 'Loading'], ['Repair_Center_Zone3_593', 41.644, 3.274, 10, 'Unloading'],
['Train_Station_Zone1_594', 40.726, -9.068, 34, 'Loading'], ['Warehouse_Zone1_595', 40.102, '-9.672', 78, 'Unloading'], ['Suburban_House_Zone3_596', 41.115, 3.022, 12, 'Loading'],
['Store_Zone2_597', 44.318, 13.515, 8, 'Unloading'], ['Warehouse_Zone3_598', 41.105, 3.376, 59, 'Loading'], ['Warehouse_Zone2_599', 45.562, 13.249, 42, 'Unloading']]

# Example Test

d = Drone("Drone_A", 5, 1000000)

d.load_destinations(data)

origin = ['Warehouse_Zone3_598', 41.105, 3.376, 59, 'Loading']
destination = ['Warehouse_Zone2_599', 45.562, 13.249, 42, 'Unloading']

d.update_path(origin, destination, 500000)

print("Current Path:", d.current_path)

recharge = d.check_trip(
    density=1.225,
    speed=5,
    b1_to=80.4, b0_to=13.8,
    b1_ld=71.5, b0_ld=-24.3,
    b1_cr=68.9, b0_cr=16.8
)

print("Recharge needed at:", recharge)