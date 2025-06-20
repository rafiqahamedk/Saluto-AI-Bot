import os
from flask import Flask, request, render_template_string
from pyngrok import ngrok, conf
from crewai import Agent, Task, Crew
from crewai.process import Process

os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
conf.get_default().auth_token = "your-ngrok-auth-token"

app = Flask(__name__)
history = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["query"]

        answer_agent = Agent(
            role="Answer Expert",
            goal="Answer user queries accurately and informatively.",
            backstory="A well-trained AI who delivers detailed explanations in simple language."
        )

        task1 = Task(
            description=f"Answer the user query: {question}",
            expected_output="A detailed but easy-to-read answer",
            agent=answer_agent
        )

        crew1 = Crew(
            agents=[answer_agent],
            tasks=[task1],
            process=Process.sequential
        )
        result1 = str(crew1.kickoff())

        summarizer_agent = Agent(
            role="Summarizer",
            goal="Summarize long answers into concise bullet points.",
            backstory="An efficient assistant who extracts key points from content."
        )

        task2 = Task(
            description=f"Summarize this answer into 3–5 bullet points:\n\n{result1}",
            expected_output="Bullet point summary",
            agent=summarizer_agent
        )

        crew2 = Crew(
            agents=[summarizer_agent],
            tasks=[task2],
            process=Process.sequential
        )
        result2 = str(crew2.kickoff())

        history.append({
            "question": question,
            "answer": result1,
            "summary": result2
        })

    return render_template_string("""
    <html><head><title>Smart Query Chat</title></head><body>
    <h1>Ask Me Anything 💬</h1>
    <form method='post'>
        <textarea name='query' rows='4' cols='50'></textarea><br>
        <button type='submit'>Submit</button>
    </form>
    {% for item in history %}
        <h2>❓ Question</h2><p>{{ item.question }}</p>
        <h2>📝 Full Answer</h2><p>{{ item.answer }}</p>
        <h2>📌 Summary</h2><ul>
        {% for line in item.summary.splitlines() %}
            <li>{{ line }}</li>
        {% endfor %}
        </ul>
        <hr>
    {% endfor %}
    </body></html>
    """, history=history)

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print("🔗 Public URL:", public_url)
    app.run(port=5000)
