from dataclasses import dataclass
from dataclasses_json import dataclass_json

from simleague.observer.observer import Observer
from abc import ABC, abstractmethod


@dataclass_json
@dataclass
class IChampion(ABC, Observer):
    @abstractmethod
    def attack_q(self) -> None:
        pass

    @abstractmethod
    def attack_w(self) -> None:
        pass

    @abstractmethod
    def attack_e(self) -> None:
        pass

    @abstractmethod
    def attack_r(self) -> None:
        pass
