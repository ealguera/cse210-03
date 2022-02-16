from operator import le


class Hider:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self.hint=[]
        self._word = []
        #self._distance = [0, 0] # start with two so get_hint always works
    
   
    def _hint(self,word):
        """Whether or not the letter has a match.

        Args:
            self (word generator): An instance of word generator.
            letter the input of the user.
        Returns:
            boolean: True if the letter is match in the word; false if otherwise.
        """ 
        self._word = word
        for x in self._word:
            self.hint += '_'
        
        return self.hint
    
    def _seeker(self, letter):
        
        for let in range(len(self._word)):
            if letter == self._word[let]: self.hint[let] = letter
        
        return self.hint