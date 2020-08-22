# pip install spacy
# python -m spacy download en_core_web_sm

import spacy
# import en_core_web_sm

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")
spacy.load('en')
spacy.load('en_core_web_lg')
# nlp = en_core_web_sm.load()
# Process whole documents
text = ("Tesco plc , trading as Tesco, is a British multinational groceries and general merchandise retailer with headquarters in Welwyn Garden City, Hertfordshire, England, United Kingdom. It is the third-largest retailer in the world measured by gross revenues and the ninth-largest in the world measured by revenues. It has shops in seven countries across Asia and Europe, and is the market leader of groceries in the UK (where it has a market share of around 28.4%), Ireland, Hungary and Thailand. Tesco was founded in 1919 by Jack Cohen as a group of market stalls in Hackney, London. The Tesco name first appeared in 1924, after Cohen purchased a shipment of tea from T. E. Stockwell and combined those initials with the first two letters of his surname, and the first Tesco shop opened in 1931 in Burnt Oak, Barnet. His business expanded rapidly, and by 1939 he had over 100 Tesco shops across the country.")

doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)