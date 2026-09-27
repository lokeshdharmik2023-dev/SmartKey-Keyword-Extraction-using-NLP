from rake_nltk import Rake

# Create RAKE object
r = Rake()

print("===== SmartKey: NLP Keyword Extractor =====")

text = input("\nEnter your paragraph:\n")

# Extract keywords
r.extract_keywords_from_text(text)

# Get keywords with scores
keywords = r.get_ranked_phrases_with_scores()

print("\nImportant Keywords:")

if keywords:
    for score, keyword in keywords[:10]:
        print(f"- {keyword}  (Score: {score:.2f})")
else:
    print("No keywords found.")