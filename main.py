from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

def reply(user):
    s = sentiment(user)[0]
    label, score = s['label'], s['score']
    base = "I’m here for you. " if label == "NEGATIVE" and score > 0.8 else ""
    tips = {
        "NEGATIVE":"It sounds tough. Want to talk about it or do a short breathing exercise?",
        "POSITIVE":"That’s great! Want me to set a reminder to keep this momentum?",
        "NEUTRAL":"Got it. How can I help further?"
    }
    return base + tips.get(label, "I’m listening.")

if __name__ == "__main__":
    print("Emotion-aware chat. Type 'exit' to quit.")
    while True:
        u = input("You: ")
        if u.lower() == "exit": break
        print("Assistant:", reply(u))
