class Language:
    def __init__(self, name) -> None:
        self.name = name
    
    def get_name(self):
        return self.name
    
    def message(self):
        print(f"My name is {self.name}")
  

languages = [Language("Python"), Language("JavaScript")]

for language in languages:
    language.message()