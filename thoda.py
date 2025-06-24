import time

def countdown_timer(seconds):
    print("Countdown Timer:")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\r", timer, end="")
        time.sleep(1)
        seconds -= 1
    
    print("\nTime's up!")

if __name__ == "__main__":
    seconds = int(input("Enter the number of seconds for the countdown timer: "))
    countdown_timer(seconds)