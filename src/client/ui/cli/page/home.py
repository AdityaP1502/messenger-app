from ui.cli.page.page import Page

class HomePage(Page):
  def __init__(self):
    super().__init__()
  
  @staticmethod
  def __get_content(data: list[str, str] = ...) -> str:
    content = """   Welcome to Aditya Messenger
    Chat:
    """ 

    # get all chat recent data 
    return content
  
  @staticmethod
  def __get_prompt() -> str:
    prompt = "Who do you want to chat:"
    return prompt
  
  def get_page(self) -> str:
    return super().get_page()
  
  
    
  