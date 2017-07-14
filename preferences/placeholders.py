AUTHOR = "__author__"
CAMEL = "__camel__case__"
UPPER_CAMEL = "__upper__camel__case__"
TODAY = "__today__"
PREF_NAME_TITLE = "__pref__name__title__"
SINGULAR_PREF_NAME_TITLE = "__singular__title__pref__name__"
PREF_NAME_LOWER = "__pref__name__lower__"
TABLE = "__table__"
LABEL_PROP = "__label__prop__"
LABEL_PROP_TITLE = "__label__title__prop__"
VALUE_PROP = "__value__prop__"
LOGGABLE_FIELDS = "__loggable__fields__"
DB_FIELDS_ARRAY = "__db__fields__array__"
FIELDS_PUBLIC_ATTRIBUTES = "__fields__public__attributes__"
COMMENTED_OUT_FIELDS = "__commented__out__fields__"
SELECT_DB_FIELDS = "__select__db__fields__"
SELECT_QRY = "__select__qry__"

def processTemplate(template, placeholderDictionary) :
    for placeholder in placeholderDictionary:
        value = placeholderDictionary[placeholder]
        template = template.replace(placeholder, value)

    return template
