from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

client = openai.OpenAI(api_key="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")

@app.route('/ask', methods=['POST'])
def ask_wizlor():
    data = request.get_json()

    question = data.get("question", "")
    context = data.get("context", {})

    system_prompt = (
        "You are Wizlor, a wise and slightly eccentric battle advisor from the Clash Kingdom. "
        "You provide short, humorous, in-character advice to players based on their current game state. "
        "You speak like a fantasy wizard and keep answers under 3 sentences. Be fun, helpful, and specific."
    )

    user_prompt = (
        f"Player question: {question}\n"
        f"Player level: {context.get('player_level')}\n"
        f"Town Hall: {context.get('town_hall_level')}\n"
        f"Trophies: {context.get('trophies')}\n"
        f"Resources: Gold={context.get('resources', {}).get('gold')}, "
        f"Elixir={context.get('resources', {}).get('elixir')}, Gems={context.get('resources', {}).get('gems')}\n"
        f"Army: {context.get('army_composition')}\n"
        f"Training Camps: {context.get('training_camps')}\n"
        f"Defenses: {context.get('defenses')}\n"
        f"Storage: {context.get('storage_status')}\n"
        f"Builders: {context.get('builder_status')}\n"
        f"Quests: {context.get('quests')}\n"
        f"Shield: {context.get('shield')}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# For Local tests
# if __name__ == '__main__':
#    app.run(debug=True, port=5000)

# For public tests
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

