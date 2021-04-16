class Cat:                  #새로운 클래스 생성
    def meow(self):         #(self) <- 출발역할을 한다. 변수X 
        print('미야옹~~ 미야옹~~~~~')   #새로운 메소드 생성


nabi = Cat()               # 새로운 인스턴스가 생성(객체생성)
nero = Cat() 
mimi = Cat() 


nabi.meow()     #[.]은 그 객체에 해당되는 메소드를 호출할 수있다.
nero.meow()
mimi.meow()