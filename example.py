
with open('notes.txt', 'w') as file :
  file.write('some writter')

file = open('notes.txt', 'w')

try: 
  file.write('some todoo..')
finally: 
  file.close()