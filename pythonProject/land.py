class Land :
    def __init__(self,location, scape, type,price,year):
        self.location = location
        self.scape = scape
        self.type = type
        self.price = price
        self.year = year

    def info(self):
        print("건물위치 :", self.location,
              "\n건물크기 :", self.scape,
              "\n건물종류 :",self.type,
              "\n건물가격 :",self.price,
                "\n시공연도 :",self.year)

my_land = Land("구로디지털단지","25평","빌라","2억","2008")
print(my_land.info())