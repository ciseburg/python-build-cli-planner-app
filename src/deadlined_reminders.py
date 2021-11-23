from abc import ABCMeta, abstractmethod
from abc import ABC
from collections.abc import Iterable
from datetime import datetime
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass

class DeadlinedReminder(Iterable, ABC):

    @abstractmethod
    def is_due(self):
        pass

#Derived class
class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text

    # Overriding base class
    def is_due(self):
        # return super().is_due()
        if self.date <= datetime.now():
            return True
        else:
            return False
    
    def __iter__(self):
        text = self.text
        formatted_date = self.date.isoformat()
        return iter([text, formatted_date])
