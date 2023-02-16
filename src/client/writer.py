import sys
from threading import Thread
from typing import Any, Callable, Iterable, Mapping

from src.client.client import Client

class Writer(Thread):
  def __init__(self, group: None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
    super().__init__(group, self.write_to_console, name, args, kwargs, daemon=daemon)
    
  def start(self) -> None:
    return super().start()
    
  def join(self, timeout: float | None = None) -> None:
    return super().join(timeout)
  
  def write_to_console(self, client : Client):
    
    if not client.message_buffer.empty():
      data = client.message_buffer.get()
      prompt = client.get_current_prompt()
      sys.stdout.write("{} sent {}\n{}".format(data[1], data[2], prompt))
    
  