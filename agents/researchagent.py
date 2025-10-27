import wikipedia

class ResearchAgent:
    def __init__(self):
        pass

    def act(self, topic):
        try:
            results = wikipedia.search(topic)
            summaries = []
            for r in results[:5]:
                try:
                    page = wikipedia.page(r)
                    summaries.append({
                        "title": page.title,
                        "summary": page.summary[:500],
                        "url": page.url
                    })
                except Exception:
                    continue
            return summaries
        except Exception as e:
            return [{"title": topic, "summary": str(e), "url": ""}]
