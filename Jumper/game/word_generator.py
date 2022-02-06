import random

class Word_generator:
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
        self._word = random.choice("Hello", "World", "Programming", "Encapsulation", "Abstraction", "Parrish", "Mexico", "Code", "Covid", "Omicron")
        self._distance = [0, 0] # start with two so get_hint always works
    
   
    def is_match(self,letter):
        """Whether or not the hider has been found.

        Args:
            self (word generator): An instance of word generator.
            letter the input of the user.
        Returns:
            boolean: True if the letter was found in the word; false if otherwise.
        """        
                  
        return  (letter in(self._word))
        
    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)