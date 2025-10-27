import os
import time
import json
from agents.researchagent import ResearchAgent
from agents.writeragent import WriterAgent
from agents.criticagent import CriticAgent
from utils.logger import Logger
from textstat import flesch_reading_ease

def main(topic=None):
    logger = Logger()
    if not topic:
        topic = input("Enter topic: ")

    os.makedirs("outputs", exist_ok=True)
    start_time = time.time()

    research_agent = ResearchAgent()
    writer_agent = WriterAgent()
    critic_agent = CriticAgent()

    logger.log(f"Starting research on topic: {topic}")
    sources = research_agent.act(topic)
    logger.log(f"Research complete: {len(sources)} sources found")

    draft = writer_agent.act(sources)
    logger.log("Initial draft completed")

    for i in range(2):
        logger.log(f"Critique round {i+1} started")
        feedback = critic_agent.act(draft)
        draft = writer_agent.revise(draft["draft"], feedback["critique"])
        logger.log(f"Revision {i+1} completed")

    final_text = draft["draft"]
    logger.log("Final draft completed")

    with open("outputs/final_article.txt", "w", encoding="utf-8") as f:
        f.write(final_text)

    metrics = {
        "topic": topic,
        "word_count": len(final_text.split()),
        "readability": flesch_reading_ease(final_text),
        "runtime_sec": round(time.time() - start_time, 2),
    }

    with open("outputs/metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    logger.log(f"Pipeline complete. Metrics saved to outputs/metrics.json")

if __name__ == "__main__":
    main()
