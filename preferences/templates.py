import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
controllerTemplate = None
actionTemplate = None
viewTemplate = None
daoTemplate = None

base = dir_path + '/templates'

with open(base + '/controller-template.php', 'r') as file :
  controllerTemplate = file.read()
  file.close()

with open(base + '/action-template.php', 'r') as file :
  actionTemplate = file.read()
  file.close()

with open(base + '/DAO-template.php', 'r') as file :
  daoTemplate = file.read()
  file.close()

with open(base + '/view-template.php', 'r') as file :
  viewTemplate = file.read()
  file.close()

with open(base + '/router-template.php', 'r') as file :
  routerTemplate = file.read()
  file.close()

with open(base + '/prefItem.html', 'r') as file :
  itemComponentTemplate = file.read()
  file.close()

with open(base + '/prefTemplate.html', 'r') as file :
  prefComponentTemplate = file.read()
  file.close()



