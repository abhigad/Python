import spacy
from sqlparse import sql, tokens as T

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define the English statement
english_statement = "Give me all products from US marketplace in the Apparel category, updated in last 24 hours"

# Parse the English statement using spaCy
doc = nlp(english_statement)

# Initialize the SQL query
sql_query = sql.Statement()

# Define the SQL query tokens
sql_query.tokens = [
    sql.Token(T.Keyword, "SELECT"),
    sql.Token(T.Wildcard, "*"),
    sql.Token(T.Keyword, "FROM"),
    sql.Token(T.Name, "Products"),
    sql.Token(T.Keyword, "WHERE"),
]

# Iterate through the parsed tokens and add conditions to the SQL query
for token in doc:
    if token.dep_ == "dobj":
        sql_query.tokens.append(sql.Token(T.Name, token.text))
    elif token.dep_ == "pobj":
        sql_query.tokens.append(sql.Token(T.Operator, "="))
        sql_query.tokens.append(sql.Token(T.String.Single, token.text))
    elif token.dep_ == "attr":
        sql_query.tokens.append(sql.Token(T.Operator, ">"))
        sql_query.tokens.append(sql.Token(T.Name, "currentdate-1"))

# Convert the SQL query tokens to a string
#The error you're encountering is likely due to a mismatch between the version of spaCy you have installed and the version of the language model you're trying to use.
# The to_unicode method was removed in spaCy v3.0, which is likely the version you're using.
#pip install spacy==2.3.5
#python -m spacy download en_core_web_sm==2.3.1        
#sql_code = sql_query.to_unicode()

sql_code = sql_query

# Print the SQL code
print(sql_code)

#
# Python's string type uses the Unicode Standard for representing characters, 
# which lets Python programs work with all these different possible characters. Unicode (https://www.unicode.org/) is 
# a specification that aims to list every character used by human languages and give each character its own unique code
#