"""
we audited 130 k samples and built a repository of 125k+ labels in 2023, based on this we can develop an 

Abuse Lookup Repository [ALR] = for example, if we provide an abusive text / text => we can return matching top N MOs with probability score of matching

this can be integrated with - 1) Pandora , 2) EDM Dashboard and 3) Paragon and relvant investigator tools

It could be early warning indiactor of abuse in the underlying unstructured data like PDP title / description / bullet points

requirment - 1) lambda , 2) QS UI , 3) API endpoint , 4) JSON wrapper and 5) stress / load testing and junk list to filter out junk words such as 

{the,and,is,of,in,to,it,for,that,with,as,was,on,at,by,are,be,this,an,or}

Additionally, we  might consider adding domain-specific stop words 
or words that don't carry significant meaning for abuse specific use case. For example, this is cheap product , word cheap is a stop word and adds little value 
in identifying an abuse

Note stop words will impact the performance of your text processing algorithms, so it's often beneficial to experiment
 and iterate based on the characteristics of labled data.

 Risk : will introduce indictor bias / suggesation bias

 Pro : a decent replacement for regex driven logic 

"""

from difflib import SequenceMatcher

def suggest_matching_themes(keyword, label_corpus, top_n=3):
    """
    Suggest top N matching themes based on the provided keyword and label corpus.

    Parameters:
    - keyword (str): The user-provided keyword.
    - label_corpus (list): List of labeled themes.
    - top_n (int): Number of top suggestions to provide.

    Returns:
    - List of top N matching themes.
    """
    # Calculate similarity scores between the keyword and each label in the corpus
    similarity_scores = [(label, SequenceMatcher(None, keyword, label).ratio()) for label in label_corpus]

    # Sort the labels based on similarity scores in descending order
    sorted_labels = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print(sorted_labels)
        

    # Extract the top N matching themes
    top_matching_themes = [label for label in sorted_labels[:top_n]]

    return top_matching_themes

# Example usage:
# Replace `label_corpus` with your actual list of labeled themes
label_corpus = ["Technology", "Artificial Intelligence", "Data Science", "Machine Learning", "Cloud Computing","Algorithms","Statistics","Supervised","unsupervised",
                "LLM","GenAI","AI","Linear Regression","Normal Distribution","Sampling","Population",
                "Outlier","Probability","Regression","A/B Testing","data analysis", "machine learning","web development","smart analytics","parallel processing",
    "python programming","software engineering","data science","cybersecurity","mobile app development","internet of things","blockchain","natural language processing",
    "computer vision","front-end development","backend development","data visualization","algorithm design","database management","network security", "responsive design",
    "software testing","user experience design","agile methodology","full-stack development","deep learning","software architecture","big data analytics",
    "devops","quantum computing"]

# Get user input
user_keyword = input("Enter a keyword: ")

# Suggest top 3 matching themes
suggested_themes = suggest_matching_themes(user_keyword, label_corpus, top_n=3)

# Display the suggestions
print("Top Matching Themes for: " + user_keyword)
for i, theme in enumerate(suggested_themes, 1):
    print(f"{i}. {theme[0]},{'======'},{theme[1]}")

