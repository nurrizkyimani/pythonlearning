from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
  f = open(filename, 'w')

  try:
    yield f
  finally: 
    f.close()
with open_managed_file('notes.txt') as f:
  f.write('some todooo...')


# https://www.youtube.com/watch?v=YE6a31J65Rc&t=370s