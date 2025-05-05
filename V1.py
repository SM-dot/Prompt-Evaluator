# Note: Preliminary Code
import re

class PromptEvaluator:
    def __init__(self, prompt):
        self.prompt = prompt.strip()
        self.scores = {}
        self.criteria = {
            "Clarity": self.evaluate_clarity,
            "Specificity": self.evaluate_specificity,
            "Context": self.evaluate_context,
            "Completeness": self.evaluate_completeness,
            "Intent": self.evaluate_intent,
            "Constraints": self.evaluate_constraints,
            "Tone": self.evaluate_tone,
            "Ambiguity": self.evaluate_ambiguity,
            "Length": self.evaluate_length,
            "Relevance": self.evaluate_relevance,
        }

    def evaluate(self):
        print(f"\n🔍 Evaluating Prompt:\n\"{self.prompt}\"\n")
        total_score = 0
        for criterion, func in self.criteria.items():
            score, suggestion = func()
            self.scores[criterion] = (score, suggestion)
            total_score += score
            print(f"{criterion}: {score}/10")
            if score < 7:
                print(f"   ⚠️ Suggestion: {suggestion}")

        avg_score = total_score / len(self.criteria)
        print(f"\n🧠 Overall Prompt Score: {avg_score:.1f}/10")
        if avg_score >= 8:
            print("✅ This is a strong prompt!")
        elif avg_score >= 6:
            print("🟡 Decent, but could be improved.")
        else:
            print("🔴 Needs significant enhancement.")

    def evaluate_clarity(self):
        if len(self.prompt.split()) < 5:
            return 4, "Too short to convey clear intent. Add more detail."
        if "?" not in self.prompt and not self.prompt.endswith("."):
            return 6, "End with a punctuation mark to aid clarity."
        return 9, "Clear and understandable."

    def evaluate_specificity(self):
        if re.search(r"\b(something|anything|everything|stuff)\b", self.prompt):
            return 5, "Avoid vague terms; specify what you want."
        return 9, "Prompt is specific."

    def evaluate_context(self):
        if any(word in self.prompt.lower() for word in ["assuming", "given", "based on"]):
            return 9, "Prompt provides context."
        return 6, "Consider adding background or context."

    def evaluate_completeness(self):
        if any(word in self.prompt.lower() for word in ["how", "why", "what", "when", "explain", "generate"]):
            return 8, "Prompt asks for a complete answer."
        return 6, "Be clear about what you want the AI to return."

    def evaluate_intent(self):
        if "help" in self.prompt.lower() or "show me" in self.prompt.lower():
            return 9, "Intent is clear."
        return 6, "Consider stating your goal explicitly."

    def evaluate_constraints(self):
        if any(word in self.prompt.lower() for word in ["limit", "no more than", "must include", "avoid"]):
            return 9, "Prompt includes helpful constraints."
        return 6, "Add any constraints if needed (e.g., word limit)."

    def evaluate_tone(self):
        if any(word in self.prompt.lower() for word in ["please", "could you", "i'd like"]):
            return 9, "Tone is polite and professional."
        return 7, "You could add a more cooperative tone."

    def evaluate_ambiguity(self):
        vague_words = ["etc", "some", "various"]
        if any(word in self.prompt.lower() for word in vague_words):
            return 5, "Avoid ambiguous words like 'etc' or 'some'."
        return 9, "Prompt is precise."

    def evaluate_length(self):
        word_count = len(self.prompt.split())
        if word_count < 5:
            return 3, "Prompt is too short—add details."
        if word_count > 50:
            return 6, "Prompt may be too long—try to focus it."
        return 9, "Length is appropriate."

    def evaluate_relevance(self):
        if any(word in self.prompt.lower() for word in ["generate", "write", "compare", "summarize"]):
            return 9, "Prompt includes a relevant AI task."
        return 6, "Specify what kind of output or task you're expecting."

# Example usage
if __name__ == "__main__":
    prompt_input = input("Enter your AI prompt: ")
    evaluator = PromptEvaluator(prompt_input)
    evaluator.evaluate()
