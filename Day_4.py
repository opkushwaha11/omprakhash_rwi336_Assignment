# import platform
# print("Operating System:", platform.system())

# print(platform.processor)


# from fpdf import FPDF

# ref=FPDF()
# ref.add_page()
# ref.set_font("Arial",size=20)
# ref.cell(200,100,"Welcome to PDF",align="L")

# ref.output("pythonfile.pdf")

class emp:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
        
e1=emp("om",100000)
# print(e1.__name)
# print(e1.__salary)

# e1.__salary=90000
# print(e1.__salary)
print(e1._emp__name)
print(e1._emp__salary)

e1._emp__salary=500000
print(e1._emp__salary)