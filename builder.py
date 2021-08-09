from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC): 
  
  @property
  @abstractmethod
  def product(self) -> None:
    pass

  @abstractmethod  
  def produce_part_a(self) -> None: 
    pass  
  
  def produce_part_b(self) -> None:
    pass
  
  def produce_part_c(self) -> None:
    pass


