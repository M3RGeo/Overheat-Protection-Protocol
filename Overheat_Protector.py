import os
import time
import pyautogui

# Function to bring the current window to focus
def bring_current_window_to_focus():
    pyautogui.hotkey('alt', 'tab')

# Function to display the initial message
def display_message(minutes=5):
    print("Computer is reaching a critical temperature. Please save your work and prepare for an emergency shutdown to avoid damaging the computer.")
    print(f"Emergency Shutdown Commencing in {minutes} Minutes")

# Function to perform the countdown and initiate shutdown
def countdown_start(minutes):
    total_seconds = minutes * 60

    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        print(f"Time remaining: {minutes} minutes {seconds} seconds", end='\r')
        time.sleep(1)
        total_seconds -= 1

    os.system('shutdown /s /f /t 0')

# Main function to orchestrate the script
def main():
    os.system('title Overheat Protection Protocol')
    display_message()

    while True:
        user_option = input("Please confirm to continue to emergency shutdown? (Y/N): ").strip().upper()

        if user_option in ('Y', 'YES'):
            countdown_start(5)  # You can change the countdown time here
            break
        elif user_option in ('N', 'NO'):
            print("Aborting Emergency Shutdown Protocol and closing the program.")
            time.sleep(10)
            exit(0)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    # Bring the current window to focus before starting
    bring_current_window_to_focus()

    # Entry point of the script
    main()