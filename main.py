from gpiozero import DigitalInputDevice   # 가스 센서의 디지털 입력 신호를 처리하기 위한 클래스
from gpiozero import OutputDevice         # 부저를 제어하기 위한 출력 장치 클래스
import time                               # 반복 실행 간 시간 지연을 주기 위한 라이브러리
bz = OutputDevice(18)         # GPIO 18번핀을 출력으로 설정하여 부저를 연결함
gas = DigitalInputDevice(17)  # GPIO 17번핀을 입력으로 설정하여 가스센서를 연결함
try:
    while True:  # 센서상태를 지속적으로 확인하기 위해 무한 반복 수행
        if gas.value == 0:  # 센서 출력이 LOW일 경우 가스가 감지된 상태로 판단
            print("가스 감지됨")  # 가스 감지 상태를 터미널에 출력
            bz.on()  # 부저를 작동시켜 경고음을 발생시킴
            
        else:  # 센서 출력이 HIGH일 경우 정상 상태로 판단
            print("정상")  # 정상 상태를 터미널에 출력
            bz.off()  # 부저를 정지시켜 소리가 나지 않도록 함

        time.sleep(0.2)  # 일정 시간 간격으로 반복 실행하여 과도한 출력 발생을 방지함

except KeyboardInterrupt:  # 사용자가 프로그램을 강제로 종료할 경우 발생하는 예외 처리
    pass  # 예외 발생 시 추가 동작 없이 프로그램을 종료함

bz.off()  # 프로그램 종료 시 부저를 꺼서 안전하게 마무리함
