# 클레스나 함수는 직접 import 불가능
# import travel.tailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
