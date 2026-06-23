# This simulates how you'd use these techniques
# In real internship you'd replace these with actual API calls

def zero_shot(review):
    return f"""
You are a sentiment analyzer.
Classify as positive or negative. Reply with ONE word only.

Review: "{review}"
Sentiment:"""

def few_shot(review):
    return f"""
Examples:
"Amazing product great quality" → positive
"Terrible broke immediately" → negative
"Fast delivery loved it" → positive
"Worst purchase ever" → negative

Classify: "{review}"
Sentiment:"""

def chain_of_thought(review):
    return f"""
Analyze step by step:
1. Positive words/phrases found?
2. Negative words/phrases found?
3. Which is stronger?
4. Final sentiment?

Review: "{review}"
Analysis:"""

def system_prompt():
    return """You are a review analysis API.
Always respond in this exact JSON format:
{
  "sentiment": "positive/negative",
  "confidence": "high/medium/low", 
  "key_phrases": ["phrase1", "phrase2"],
  "suggested_rating": 1-5
}"""

# Test all techniques
reviews = [
    "The product looks great but stopped working after 2 days",
    "Absolutely fantastic best purchase of my life",
    "Okay product nothing special average quality"
]

for review in reviews:
    print("=" * 60)
    print(f"REVIEW: {review}")
    print(f"\nZero-shot prompt:\n{zero_shot(review)}")
    print(f"\nFew-shot prompt:\n{few_shot(review)}")
    print(f"\nCoT prompt:\n{chain_of_thought(review)}")
    print(f"\nSystem prompt:\n{system_prompt()}")