class Hangman:
  """
    The responsibility of Hangman is to display the parachute and delete the chute from top depending on the count of false boolean returns

    Attributes:
        _parachute (List[str]): List to make an image of parachute. 
  """
  def __init__(self):
    """
    Constructs parachute

    Args:
      self (Hangman): An instance of Hangman
    """
    self._parachute = [" ___ ",
                       "/___\ ",
                       "\   / ",
                       " \ / ",
                       "  O ",
                       " /|\ ",
                       " / \ "]
    self._life = 0
  
  def update_chute(self, false_count):
    """
    Updates the parachute on the count of false boolean return.
    """
    self._life += 1 if false_count == False else 0
    if self._life == 0:
      for x in range(len(self._parachute)):
        print(self._parachute[x])

    elif self._life == 4:
      print("  x \n"
            " /|\ \n"
            " / \ \n")
    else:
      for x in range(self._life, len(self._parachute)):
        print(self._parachute[x])
