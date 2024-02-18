from amazon.ion import simpleion

print("ello Gita")

# Sample Amazon Ion data as a string
ion_data = '''
{
    name: "John",
    age: 30,
    is_student: true,
    interests: ["Reading", "Hiking", "Coding"]
}
'''

# Deserialize the Ion data
ion_struct = simpleion.loads(ion_data)

# Serialize the Ion struct to JSON
json_data = simpleion.dumps(ion_struct, binary=False, indent='  ')

# Print the JSON data
print(json_data)

obj = simpleion.loads('{abc: 123}')

print(obj['abc'])

# To serialize an Amazon Ion stream to JSON in Python, you can use the ion-python library, 
# which provides the capability to work with Amazon Ion data. You can install the library using pip:

##Amazon Ion is a way to store and share information in a special format that's easy for computers to read. 
# It's like putting data into neatly organized containers, and these containers can hold all kinds of information.

# Let's imagine two situations to explain Ion in a way a 5th grader can understand:

# Retail: Suppose you're keeping track of items in a store. Each item has a name, price, and maybe a description. With Ion, you can put this information into a special box, and the box has labels for each piece of information. So, if you have a toy, you can put its name, price, and description into this box. Now, when you want to find information about the toy, you just look in the right box, and everything is neatly organized.

# For example:

# In the "Toy" box, there's a label that says "Name," and under it, you might find "LEGO Set."
# There's another label that says "Price," and under it, you see "$20.00."
# This makes it easy to find and understand the details about the toy.
# Finance: Imagine you have a piggy bank, and you want to keep track of how much money you have saved. Instead of just putting all your coins together, you put them in separate jars. Each jar is labeled with the type of coin - pennies, nickels, dimes, and quarters. This way, you can see exactly how much money you have in each type of coin.

# For example:

# In the "Pennies" jar, you have 25 pennies, which makes 25 cents.
# In the "Nickels" jar, you have 10 nickels, which is 50 cents.
# This helps you keep track of how much money you have saved in different types of coins.
# So, Amazon Ion is like those labeled boxes or jars. It helps us store information in a way that's easy 
# for computers to understand and organize, whether it's details about products in a store or 
# money in your piggy bank. It's all about keeping things neat and tidy so we can find what we need quickly.