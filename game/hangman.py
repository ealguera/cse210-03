class Hangman:
  def __init__(self):
    self._error = 0
    self._man=  ['''
 ___
/___\\
\   /
 \ /
  O
 /|\\
 / \\
''',
'''
/___\\
\   /
 \ /
  O
 /|\\
 / \\
''',
'''
\   /
 \ /
  O
 /|\\
 / \\
''',
'''
 \ /
  O
 /|\\
 / \\
''',
'''
  x
 /|\\
 / \\
''']

  @property
  def error(self):
    return self._error

  @error.setter
  def error(self, error):
    self._error = error

  @property
  def man(self):
    return self._man