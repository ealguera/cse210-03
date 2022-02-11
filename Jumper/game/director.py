from game.terminal_service import TerminalService
from game.hangman import Hangman
from game.word_generator import Word_generator 
from game.hider import Hider

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word_generator = Word_generator()
        self._is_playing = True
        self._is_letter_matching = False # this will hold the boolean value. that we can use as input for the method to delete the parachut lines
        self._hangman = Hangman()
        self._terminal_service = TerminalService()
        self._hider = Hider()

        # make the hint 
        self.hint = self._hider._hint(self._word_generator._word)
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self.letter = self._terminal_service.read_number("\nGuess a letter [a-z]: ")
        self._is_letter_matching = self._word_generator.is_match(self.letter)
        #self._seeker.move_location(new_location)

        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        #self._hider.watch_seeker(self._seeker)
        self._hangman.update_chute(self._is_letter_matching)
        self._terminal_service.write_text(self._hider._word)

       
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """

        self.hint = self._hider._seeker(self.letter)
        self._terminal_service.write_text(''.join(self.hint))
        if self._hangman._life >= 4:
            self._is_playing = False
            self._terminal_service.write_text("game over!")
