class FourCal:
    
     def __init__(self, first, second):
         self.first = first
         self.second = second

     def add(self):
         result = self.first + self.second
         return result

     def mul(self):
         result = self.first * self.second
         return result

     def sub(self):
         result = self.first - self.second
         return result

class FourCal_div(FourCal):                 
    def div(self):
        result = self.first / self.second
         return result

#새로운 클라스에서 처음 클라스를 인자로 집어넣으면
#기능을 사용할 수있다.

#0으로 나누면 오류가 발생한다. 조건문을 하나 더 추가해야한다.
#상속하면 내용을 추가 작성하는 것도 가넝

div_data = FourCal(4, 2)

