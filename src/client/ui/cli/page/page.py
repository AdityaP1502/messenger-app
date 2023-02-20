import os
import platform

class Page():
  def __init__(self):
    self.state = 0
    
  @staticmethod
  def __get_content(data : list[str, str] = []) -> str:
    pass
  
  @staticmethod
  def __get_prompt() -> str:
    pass
  
  def get_page(self) -> str:
    content = self.__get_content()
    prompt = self.__get_prompt()
    
    return content + "\n" + prompt
  
  def set_state(self, new_state : int) -> None:
    self.state = new_state

class PageLoader():
  def __init__(self, page) -> None:
    self.__loaded_page = page
  
  def show(self) -> None:
    page = self.__loaded_page.get_page()
    print(page)
    
  def clear(self) -> None:
    if platform.system() == "Windows":
      os.system(command="cls")
      
  def update(self, page) -> None:
    self.clear()
    self.show()
    
  def load_new_page(self, new_page : Page) -> None:
    self.__loaded_page = new_page
  
  def get_loaded_page(self) -> Page:
    return self.__loaded_page
  
class UserInputHandler():
  @staticmethod
  def process_home_input(user_input : str, page_loader : PageLoader):
    parsedInput = user_input.split(":", 1)
    if len(parsedInput > 1):
      command, argument = parsedInput
      if command == "CHAT":
        NotImplemented
    
    else:
      # other command that don't require an argument
      NotImplemented
  
  @staticmethod
  def process_chat_input(user_input : str, page_loader : PageLoader):
    NotImplemented
  
  @staticmethod
  def process_incoming_call_input(user_input : str, curr_page : Page, history : list[Page], page_loader : PageLoader):
    if user_input == "y":
      # send a received request to server
      # change page to OnCallPage
      history.append(curr_page)
      pass
    
    elif user_input == "n":
      # send a declined request to server
      # back to prev page
      pass
  
  @staticmethod
  def process_on_call_input(user_input : str, history : list[Page], page_loader : PageLoader):
    if user_input == "HANG":
      # send a HANG request to server
      # change page back from history
      curr_page = history.pop()
      NotImplemented
    
  @staticmethod
  def process_user_input(user_input : str, curr_page : Page, page_loader : PageLoader, history : list[Page]):
    NotImplemented

