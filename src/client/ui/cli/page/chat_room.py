from ui.cli.page.page import Page

class ChatRoomPage(Page):
  def __init__(self, recipient_username : str) -> None:
    super().__init__()
    self.recipient_username = recipient_username
  
  @staticmethod
  def __get_content(data: list[str, str] = ...) -> str:
    NotImplemented
  
  @staticmethod
  def __get_prompt() -> str:
    NotImplemented
    
  def get_page(self) -> str:
    return super().get_page()
  
    
  
  