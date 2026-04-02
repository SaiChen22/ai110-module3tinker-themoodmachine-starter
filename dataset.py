"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
]

SAMPLE_POSTS.extend([
    "Lowkey stressed but still proud of how far I have come",
    "No cap, this playlist is amazing 😂",
    "I absolutely love getting stuck in traffic for an hour",
    "Finals week got me tired and upset :(",
    "Highkey feeling good today :)",
    "That meeting could have been an email",
    "I laughed so hard I cried 💀",
    "Got the internship, but now I am terrified",
    "The weather is just weather today",
    "Lost my keys again, awesome",
])

TRUE_LABELS.extend([
    "mixed",     # "Lowkey stressed but still proud of how far I have come"
    "positive",  # "No cap, this playlist is amazing 😂"
    "negative",  # "I absolutely love getting stuck in traffic for an hour"
    "negative",  # "Finals week got me tired and upset :("
    "positive",  # "Highkey feeling good today :)"
    "neutral",   # "That meeting could have been an email"
    "positive",  # "I laughed so hard I cried 💀"
    "mixed",     # "Got the internship, but now I am terrified"
    "neutral",   # "The weather is just weather today"
    "negative",  # "Lost my keys again, awesome"
])
