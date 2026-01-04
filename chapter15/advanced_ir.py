import RPi.GPIO as GPIO
from time import time, sleep

# 各ボタンの状態
status1 = 0
status2 = 0
status3 = 0

# 使用する GPIO ピン（BCM 番号）
IR_PIN = 21

# リモコンのボタンコード（NECフォーマット）
KEY_1 = 0xff30cf
KEY_2 = 0xff18e7
KEY_3 = 0xff7a85


def setup():
    """GPIO の初期設定"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # FALLING エッジを検出するイベントを登録
    GPIO.add_event_detect(IR_PIN, GPIO.FALLING, bouncetime=50)

    print("GPIO 初期化完了（BCM モード）")


def binary_aquire(pin, duration):
    """指定時間だけ高速に GPIO を読み取る"""
    t0 = time()
    results = []
    while (time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results


def on_ir_receive(pinNo, bouncetime=150):
    """赤外線信号を解析してコードを返す"""
    data = binary_aquire(pinNo, bouncetime / 1000.0)
    if len(data) < bouncetime:
        return

    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0

    for i in range(1, len(data)):
        if (data[i] != data[i - 1]) or (i == len(data) - 1):
            pulses.append((data[i - 1], int((i - i_break) / rate * 1e6)))
            i_break = i

    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"

    try:
        return int(outbin, 2)
    except ValueError:
        return None


def destroy():
    """GPIO の後処理"""
    GPIO.cleanup()
    print("GPIO を解放しました。終了します。")


# ---------------------------------------------------------
# メイン処理
# ---------------------------------------------------------
if __name__ == "__main__":
    setup()

    try:
        print("赤外線リモコン受信を開始します。Ctrl+C で終了できます。")

        while True:
            # イベントが発生したかチェック
            if GPIO.event_detected(IR_PIN):
                code = on_ir_receive(IR_PIN)

                if code == KEY_1:
                    status1 ^= 1
                    print(f"KEY_1 を受信しました → 状態: {status1}")

                elif code == KEY_2:
                    status2 ^= 1
                    print(f"KEY_2 を受信しました → 状態: {status2}")

                elif code == KEY_3:
                    status3 ^= 1
                    print(f"KEY_3 を受信しました → 状態: {status3}")
            sleep(0.01)

    except KeyboardInterrupt:
        print("\nCtrl+C が押されました。安全に終了します。")

    finally:
        destroy()