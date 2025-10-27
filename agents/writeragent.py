from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class WriterAgent:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def act(self, sources):
        topic = sources[0]["title"] if sources else "Unknown Topic"
        source_text = "\n".join(
            [f"[{i+1}] {s['title']}: {s['summary']} ({s['url']})"
             for i, s in enumerate(sources)]
        )

        prompt = (
            f"You are a professional writer. Based on the research below, "
            f"write a detailed article (700–1200 words) about '{topic}'.\n\n"
            f"Include in-text citations using [1], [2], etc.\n\nResearch:\n{source_text}"
        )

        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a knowledgeable article writer."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        return {"draft": response.choices[0].message.content}

    def revise(self, draft_text, critique):
        prompt = (
            "You are a writer revising your article based on editorial feedback.\n"
            f"Feedback:\n{critique}\n\n"
            "Revise the following article to address the feedback but keep the tone and structure professional:\n\n"
            f"{draft_text}"
        )

        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a skilled editor and writer."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.6,
        )

        return {"draft": response.choices[0].message.content}
