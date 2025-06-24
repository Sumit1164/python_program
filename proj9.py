import time
def countdown_timer(seconds):
    print("\n🕒 Countdown Timer 🕒")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Time Left: {timer} ⏳", end="", flush=True)
        time.sleep(1)
        seconds -= 1    
    print("\n⏰ Time's up! ⏰")
if __name__ == "__main__":
    seconds = int(input("Enter the number of seconds for the countdown timer: "))
    countdown_timer(seconds)