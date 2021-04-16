PI = 3.14
radius = float(input('반지름을 입력하세요: '))

def circle_area_circum(radius):
    area = PI * (radius ** 2)
    length = 2 * PI * radius
    return '원의 면적은 {}, 원의 둘레는 {} 입니다.' .format(area,length)

print(circle_area_circum(radius))