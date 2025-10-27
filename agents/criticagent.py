from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CriticAgent:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def act(self, draft):
        text = draft.get("draft", "")
        critique_prompt = (
            "You are an editor. Review the following article for factual accuracy, tone, and structure.\n"
            "Return JSON with two keys: 'critique' (a bullet list of issues) "
            "and 'improved_draft' (a revised version).\n\nArticle:\n" + text
        )

        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful critic and editor."},
                {"role": "user", "content": critique_prompt},
            ],
            temperature=0.5,
        )

        reply = response.choices[0].message.content
        try:
            return json.loads(reply)
        except Exception:
            return {"critique": reply, "improved_draft": text}
