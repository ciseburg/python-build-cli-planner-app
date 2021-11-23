import csv
# from src.reminder import PoliteReminder
# from src.deadlined_reminders import DateReminder
from src.deadlined_reminders import DeadlinedReminder

def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()

def add_reminder(text, date, ReminderClass):

    # reminder = PoliteReminder(text=text)
    if not issubclass(ReminderClass, DeadlinedReminder):
        raise TypeError("Invalid Reminder Class")

    reminder = ReminderClass(text=text, date=date)
   
    with open('reminders.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        # writer.writerow([reminder.text])
        writer.writerow(reminder)

