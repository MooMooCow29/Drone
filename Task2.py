# Task 2
# 100500474

def load_to_dict(data_array):

    dest = {}

    for item in data_array:

        name = item[0]
        lon = item[1]
        lat = item[2]
        alt = item[3]
        port = item[4]

        ok = True

        # duplicate check
        if name in dest:
            ok = False

        # name characters check
        for c in name:
            if not (('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9') or c == '_'):
                ok = False

        # convert numbers
        try:
            lon = float(lon)
            lat = float(lat)
            alt = float(alt)
        except:
            ok = False

        # bounds
        if ok:
            if lon < -90 or lon > 90:
                ok = False
            if lat < -90 or lat > 90:
                ok = False
            if alt < 0 or alt > 100:
                ok = False

        # port check
        if port != "Loading" and port != "Unloading":
            ok = False

        # store valid data
        if ok:
            dest[name] = [lon, lat, alt, port]

    return dest


def add_destination(dest):

    print("\nAdd a new destination")

    name = input("Enter Name: ")
    lon = input("Enter Longitude: ")
    lat = input("Enter Latitude: ")
    alt = input("Enter Altitude: ")
    port = input("Enter Port (Loading/Unloading): ")

    ok = True

    # duplicate check
    if name in dest:
        ok = False

    # name characters check
    for c in name:
        if not (('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9') or c == '_'):
            ok = False

    # convert numbers
    try:
        lon = float(lon)
        lat = float(lat)
        alt = float(alt)
    except:
        ok = False

    # bounds
    if ok:
        if lon < -90 or lon > 90:
            ok = False
        if lat < -90 or lat > 90:
            ok = False
        if alt < 0 or alt > 100:
            ok = False

    # port check
    if port != "Loading" and port != "Unloading":
        ok = False

    # store + show count
    if ok:
        dest[name] = [lon, lat, alt, port]
        print("Added successfully")
        print("Total destinations:", len(dest))
    else:
        print("Invalid input, new data - not added")

#Test Data
data = [['High_Rise_Building0', '-26.311', '30.691', 13, 'Loading'], ['Factory1', -9.675, -6.553, 35, 'Unloading'], ['Office2', -22.411, -81.009, 80, 'Loading'],
  ['Repair_Center3', '-13.689', -33.973, 654, 'Unloading'], ['Warehouse4', 63.266, 51.491, 57, 'Loading'], ['Post_Office5', 56.558, '69.42', 92, 'Unloading'],
  ['Suburban_House6', '43.167', -46.817, 38, 'Loading'], ['Store7', -55.068, 60.346, 170, 'Unloading'], ['Farm8', -43.965, 23.637, 73, 'Loading'],
  ['Depot9', '82.819', -69.104, 42, 'Unloading'], ['Post_Office10', -71.638, '-53.635', 20, 'Loading'], ['Farm11', 68.014, 55.636, 91, 'Unloading'],
  ['Suburban_House12', '-70.98', -49.888, 18, 'Loading'], ['Farm13', -74.962, 12.18, 32, 'Unloading'], ['Store14', -72.929, 43.949, 50, 'Loading'],
  ['Farm15', '9.37', '-53.119', 196, 'Unloeading'], ['High_Rise_Building16', 69.554, -22.268, 73, 'Loading'], ['Depot17', -50.27, 15.165, 12, 'Unloading'],
  ['Store18', '-6.502', 84.375, 75, 'Loadddding'], ['Suburban_House19', 45.372, -15.979, 89, 'Unloading'], ['Factory20', -2.899, '-16.617', 89, 'Loading'],
  ['High_Rise_Building21', '39.197', -57.132, 23, 'Unloading'], ['Warehouse22', 47.577, -30.891, 70, 'Loading'], ['Farm23', -26.157, -56.683, 87, 'Unloading'],
  ['Factory24', '63.95', -28.562, 648, 'Loading'], ['Factory25', -16.763, '-68.-314', 91, 'Unloading'], ['Office26', 88.407, -86.797, 27, 'Loading'],
  ['Store27', '-80.927', 81.929, 77, 'Unloading'], ['Train_Station28', -4.365, 10.022, 37, 'Loading'], ['Suburban_House29', -42.237, -13.428, 51, 'Unloading'],
  ['Post_Office30', '83.915', '43.441', 65, 'Loading'], ['Office31', 48.126, -78.267, 101, 'Unloading'], ['Factory32', -65.33, 54.775, 830, 'Loading'],
  ['Store33', '-30.318', -33.048, 56, 'Unloading'], ['Train_Station34', -65.357, 5.54, 77, 'Loading'], ['Factory35', 10.257, '-82.978', 23, 'Unloading'],
  ['Suburban_House36', '50.86.6', -34.657, 62, 'Loading'], ['Train_Station37', -13.389, 31.009, 8, 'Unloading'], ['Suburban_House38', -59.966, 44.835, 43, 'Loading'],
  ['Depot39', '34.651', 16.952, 21, 'Unloading'], ['Office2', 41.55, '-13.317', 18, 'Loading'], ['Farm41', 44.867, -53.163, 86, 'Unloading'],
  ['Depot42', '16.137', 42.286, 821, 'Loading'], ['Farm43', -15.582, 36.127, 9, 'Unloading'], ['Depot44', 18.39, -76.789, 16, 'Loading'],
  ['Depot45', '-62.336', '23.94', 10, 'Unloading'], ['Post_Office46', 34.81, 59.467, 12, 'Loading'], ['Suburban_House47', -44.244, 23.51, 92, 'Unloading'],
  ['Suburban_House29', '-73.962', -5.631, 4, 'Loading'], ['Office26', 68.361, -60.934, 28, 'Unloading']]

d = load_to_dict(data)

print("Initial destinations:", len(d))

for k in d:
    print(k, d[k])

add_destination(d)