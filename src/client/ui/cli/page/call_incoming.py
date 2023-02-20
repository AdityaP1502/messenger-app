from ui.cli.page.page import Page

class OnCallPage(Page):
  def __init__(self):
    super().__init__()
  
  @staticmethod
  def __get_content(data: list[str, str] = ...) -> str:
    NotImplemented
  
  @staticmethod
  def __get_prompt() -> str:
    NotImplemented
  
  def get_page(self) -> str:
    return super().get_page()
    
    
  