from abc import ABCMeta, abstractmethod
from abc import ABC
from collections.abc import Iterable

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due():
        pass

class DeadlinedReminder(Iterable, ABC):

    @abstractmethod
    def is_due():
        pass