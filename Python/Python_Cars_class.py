####CREATE AN OBJECT
class Tools:
    car_list=[]
    name = "Jenkins"
    version = 20
    date = "20/11"
    cartyres=4
    car_name="toyota"

    def cartyres1(self):
        if self.cartyres==4:
            self.car_list.append(self.car_name)
            print(self.car_list)
        else:
            print("Only two wheelers are there")

Toyota = Tools()
Toyota.cartyres1()
