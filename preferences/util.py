import re

""" CLASSES """
class DBField(object):
    def __init__(self, name, fieldType, loggable):
        self._name = name
        self._type = fieldType
        self._loggable = loggable

    """ 'name' getter """
    @property
    def name(self):
        return self._name

    """ 'name' setter """
    @name.setter
    def name(self, value):
        self._name = value

    """ 'type' getter """
    @property
    def type(self):
        return self._type

    """ 'type' setter """
    @type.setter
    def type(self, value):
        self._type = value

    """ 'loggable' getter """
    @property
    def loggable(self):
        return self._loggable

    """ 'loggable' setter """
    @loggable.setter
    def loggable(self, value):
        self._loggable = value

""" FUNCTIONS """
def getAdditionalFields() :
    additionalFields = []    

    print("")
    more = recursiveYesNo("would you like to add additional db fields? (y/n): ")

    while more :
        field = getNextField()
        additionalFields.append(field)
        print("")
        more = recursiveYesNo("would you like to add another field? (y/n): ")

    return additionalFields
    
def recursiveYesNo(prompt) :
    response = raw_input(prompt)

    if response == 'y':
        return True
    elif response == 'n':
        return False
    else:
        print("INVALID INPUT: must enter 'y' or 'n'")
        return recursiveYesNo(prompt)

def getNextField() :
    fieldName = raw_input("field: ")
    fieldType = raw_input("field type: ")
    loggable = recursiveYesNo("is field loggable? (y/n): ")

    return DBField(fieldName, fieldType, loggable)

def fieldsToArrayString(fields, numIndents, includeType, isCommented) :

    numFields = len(fields)
    maxNameLength = getLengthOfLongestFieldName(fields)
    result = "array(\n"

    if isCommented :
        result = indent(result, numIndents)
        result = "     *" + result

    count = 0
    for field in fields :
        line = ""

        line += '"' + field.name + '"'

        if includeType :
            offset = maxNameLength - len(field.name)
            line += (' ' * offset) + ' => "' + field.type + '"'

        if count != numFields - 1 :
            line += ","

        line += "\n"
        line = indent(line, numIndents + 1)

        if isCommented :
            line = "     *" + line

        count += 1
        result += line

    if isCommented :
        result += "     *" 
        result += indent(")", numIndents);
    else :
        result += indent(");\n", numIndents);

    return result

# each indent is 4 spaces
def indent(string, numIndents):
    
    indentation = ""
    for i in range(numIndents) :
        indentation += "    "

    return indentation + string

def getLoggableFields(fields):
    loggableFields = []

    for field in fields:
        if field.loggable == True :
            loggableFields.append(field)

    return loggableFields

def getLengthOfLongestFieldName(fields) :
    max = len(fields[0].name)
    
    for field in fields :
        length = len(field.name)
        if length > max :
            max = length

    return max

def fieldsToPublicAttributesString(fields) :
    result = ""

    for field in fields :
        result += indent("public $", 1)
        result += field.name
        result += ";\n"

    return result

def fieldsToSelectQuery(fields, prefName, table) :
    abbreviation = ""

    prefWords = prefName.split()
    for word in prefWords :
       abbreviation += word[0] 

    result = indent("SELECT\n", 4)

    count = 0
    for field in fields :
        line = abbreviation + '.' + field.name
        if count != len(fields) - 1 :
            line += ','
        count += 1

        line += '\n'

        result += indent(line, 5)

    result += indent("FROM\n", 4)

    line = table + " " + abbreviation
    result += indent(line, 5) 

    return result

def removeCodeBlocks(prefName, fileLoc, fileName, regex) :
    with open(fileLoc, 'r') as file :
        fileContents = file.read()
        file.close()

    matches = getMatchingCodeBlocks(prefName, fileContents, regex)

    if (matches != None ) :
        for codeBlock in matches :

            codeBlock = codeBlock.group()
            if (confirmRemoveCodeBlock(codeBlock, fileName)) :
                fileContents = fileContents.replace(codeBlock, '')
    else :
        print("*** Could not find code to remove from " + fileName + " ***")

    return fileContents

def confirmRemoveCodeBlock(codeBlock, fileName) :

    print("")
    print(codeBlock)
    print("")
    return recursiveYesNo("Would you like to remove the above code block from " + fileName + "? (y/n) :")

def getMatchingCodeBlocks(prefName, fileContents, regex) :
    keywords = prefName.replace(' ', '|')
    for word in prefName.split() :
        if word[-1:] == 's' :
            keywords += '|' + word[:-1]

    regex = regex.replace("__keywords__", keywords)

    return re.finditer(regex, fileContents, re.IGNORECASE)

def updatePreferenceViewDelegate(prefName, homeDir) :
    fileName = 'preferencesViewDelegate.php'
    fileLoc = homeDir + '/pestroutes/resources/delegates/settings/' + fileName
    regex = "if\(\$action == [\"|'].*?(__keywords__).*?[\"|']\){(\\r|\\n|.)+?(?=else)"

    return removeCodeBlocks(prefName, fileLoc, fileName, regex)

def updatePreferenceDelegate(prefName, homeDir) :
    fileName = 'preferencesDelegate.php'
    fileLoc = homeDir + '/pestroutes/resources/delegates/settings/' + fileName
    regex = "elseif\(\$action == [\"|'].*?(__keywords__).*?[\"|']\)(\r|\n){(\r|\n)(\r|\n|.)+?(?=elseif)"

    return removeCodeBlocks(prefName, fileLoc, fileName, regex)

def appendOriginal(newContents, fileLoc) :

    with open(fileLoc, 'r') as file :
        fileContents = file.read()
        file.close()

    before = "\n<!-- ORIGINAL -->\n<!-- "
    after = " -->"

    fileContents = fileContents.replace('<!--', '')
    fileContents = fileContents.replace('-->', '')
    fileContents = before + fileContents + after

    return newContents + fileContents

def writeToFile(fileLoc, content) :
    with open(fileLoc, 'w') as file :
        file.write(content) 
        file.close()




