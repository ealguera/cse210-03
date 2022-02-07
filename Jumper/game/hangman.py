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
  
  def update_chute(self, false_count):
    """
    Updates the parachute on the count of false boolean return.
    """
    if false_count == 0:
      for x in range(len(self._parachute)):
        print(self._parachute[x])

    elif false_count == 4:
      print("  x \n"
            " /|\ \n"
            " / \ \n")
    else:
      for x in range(false_count, len(self._parachute)):
        print(self._parachute[x])
