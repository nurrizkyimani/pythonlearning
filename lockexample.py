class ManagedFile:
  def __init__(self, filename):
    print('init')
    self.filename = filename

  def __enter__(self):
    print('enter')
    self.file = open(self.filename, 'w')
    return self.file


  def __exit__(self, exc_type, exc_value, exc_traceback):
    if self.file:
      self.file.close()
    if exc_type is not None:
      print('exception has been handling')
    print('exc:', exc_type, exc_value)
    print('exit')


with ManagedFile as file:
  print('do some stufff')
  file.write('some todo///')
  file.somemethod()
  print('continuing')