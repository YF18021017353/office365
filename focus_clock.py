import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60

        print(f"Remaining time: {minutes:02d}:{seconds:02d}")
        time.sleep(1)

    print("Time's up! Stay focused!")

# 设置专注时长为25分钟（可以根据需要进行调整）
focus_duration = 25

focus_timer(focus_duration)
