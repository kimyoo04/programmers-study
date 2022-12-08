# 클레스나 함수는 직접 import 불가능
# import travel.tailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from random import *
from travel import * # __init__.py 파일에서 __all__ 을 통해 공개설정을 해주어야 *가 적용이 된다.
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

