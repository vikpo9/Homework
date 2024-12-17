from Hist import Hist_from_csv, Hist_from_xlsx

class HistEncoder:
    def __init__(self, strategy):
        self.__strategy = strategy
    
    @property
    def strategy(self):
        return self.__strategy
    
    @strategy.setter
    def strategy(self, strategy):
        self.__strategy = strategy

    def read(self, file_path):
        self.__strategy.read(file_path)

    def write(self, file_path):
        self.__strategy.write(file_path)

    def draw(self, file_path):
        self.__strategy.draw_hist(file_path)

if __name__ == "__main__":
    obj = HistEncoder(Hist_from_csv())
    obj.read("Datas/test.csv")
    obj.draw("Datas/test_1.jpg")
    obj.write("Datas/test_1_res.csv")

    obj.strategy = Hist_from_xlsx()
    obj.read("Datas/test.xlsx")
    obj.draw("Datas/test_2.jpg")
    obj.write("Datas/test_2_res.xlsx")
