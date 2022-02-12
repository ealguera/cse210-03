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
        words=["hello", "world", "programming", "encapsulation", "abstraction", "brotherparrish", "mexico", "code", "covid", "omicron"]
        self._word = random.choice(words)
        self.letters = []
        # self._distance = [0, 0] # start with two so get_hint always works
    
   
    def is_match(self,letter):
        """Whether or not the letter has a match.

        Args:
            self (word generator): An instance of word generator.
            letter the input of the user.
        Returns:
            boolean: True if the letter is match in the word; false if otherwise.
        """    
        is_match = letter in(self._word)
        if is_match:
            self.letters.append(letter)

        return is_match
        
    
    def underscore(self):
        phase = ''
        for l in self._word:
            if l in self.letters: 
                phase += f'{l} '
            else:
                phase += "_ "
        print(phase)
    
        