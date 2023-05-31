import spacy

# Load the spaCy English language model
nlp = spacy.load('en_core_web_sm')

# Define a list of garden path sentences
gpe1 = "The complex houses married and single soldiers and their families."
gpe2 = "The horse raced past the barn fell."

gardenpathSentences = []

gardenpathSentences.append(gpe1)
gardenpathSentences.append(gpe2)
gardenpathSentences.append("Mary gave the child a Band-Aid.")
gardenpathSentences.append("That Jill is never here hurts.")
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi.")

# Iterate over each sentence in the list
for i in gardenpathSentences:
    doc = nlp(i)                                        # Tokenize the sentence using spaCy's language model
    doc.text.split()
    print(i)
    print("For tokenise:")
    print([token.text for token in doc])                # Tokenise
    print("For named entity recognition:")
    print([(i, i.label_, i.label) for i in doc.ents])   # Named entity recognition
    print("-"*100)

# Look up the explanation for two entities and print them
print(spacy.explain("PERSON"))
print(spacy.explain("GPE"))

# Write a comment about two entities that you looked up. For each entity answer the following questions:
# What was the entity and its explanation that you looked up?
# Answer: PERSON refers to people, including fictional. GPE refers to countries, cities, and states.
# Did the entity make sense in terms of the word associated with it?
# Yes, the entities make sense. PERSON is clearly associated with "people," and GPE is associated with places, such as countries and cities. This categorization likely comes from the field of geography.