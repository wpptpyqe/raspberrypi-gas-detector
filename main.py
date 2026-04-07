from gpiozero import DigitalInputDevice   # 가스 센서 입력을 위한 클래스
from gpiozero import OutputDevice         # 부저 출력 제어를 위한 클래스
import time                               # 시간 지연을 위한 라이브러리

bz = OutputDevice(18)         # GPIO 18번 핀 부저 (출력 장치)
gas = DigitalInputDevice(17)  # GPIO 17번 핀 가스 센서 (입력 장치)

try:
    while True:  # 무한 반복 → 센서 상태를 계속 확인
        if gas.value == 0:  # 센서 값이 0이면 LOW 가스 감지 상태
            print("가스 감지됨")  # 상태 출력
            bz.on()  # 부저 ON 소리 발생
        else:  # 센서 값이 1이면 HIGH 정상 상태
            print("정상")  # 상태 출력
            bz.off()  # 부저 OFF 소리 없음

        time.sleep(0.2)  # 0.2초마다 반복으로 과도한 소리 제어

except KeyboardInterrupt: 
    pass  # 예외 발생 시 아무 동작 없이 종료

bz.off()  # 프로그램 종료 시 부저 OFF
