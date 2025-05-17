# wizlor-battle-advisor

Wizlor is a smart, friendly in-game character designed to guide and engage new players in strategy games like Clash of Clans. Many users quit early because they feel lost or bored. Wizlor solves this by offering clear, tactical advice and game explanations through fun and friendly conversations. It acts like a digital companion helping players understand the game, stay motivated, and enjoy their early experience. By making players feel supported and entertained, Wizlor reduces early churn and encourages long-term engagement. Over time, it can even become a reason players return not just for gameplay, but to interact with their in-game “friend.”

Most games lack real emotional connection, causing new players to quit early. While some have scripted guides, they aren't truly engaging. Wizlor fills this gap as a fun, smart in-game companion that guides and entertains players. It helps reduce early drop-off and builds a bond that can keep players coming back—not just to play, but to connect.

Future Improvements:
Due to limited time and resources, the current version of Wizlor is a basic prototype that focuses on core interaction and concept validation. While it introduces the idea of a smart, friendly in-game guide, it doesn't yet have access to real-time game data or advanced personalization features.
In the future, Wizlor can be powered by live data from the game, allowing it to provide accurate, up-to-date insights on the player’s village, troops, attack logs, or even current meta strategies. With deeper integration, it could offer truly personalized advice, adapting to the player’s evolving style and needs.
Wizlor has the potential to become a powerful tool that combines game analytics, strategic guidance, and emotional connection, helping players stay engaged, improve their gameplay, and enjoy a more immersive experience.

Wizlor is a web-based prototype combining voice interaction with AI-powered game advice.

Frontend: Built with HTML, CSS, and JavaScript. Uses Web Speech API for voice input and Speech Synthesis API to read responses aloud. A simple UI mimics an in-game assistant.

Backend: Uses Python (Flask) with Flask-CORS for local API communication. OpenAI GPT-3.5-Turbo generates short, fun, context-aware replies.

How It Works:
Voice input → JS sends data + game context to Flask → GPT responds → JS displays and reads it back.

Game Context:
Static player data (e.g., army size, town hall level) is used to simulate personalized advice.

Context Awareness:
The prototype includes a static context (e.g., army size, builder status, town hall level) to simulate how Wizlor would give tailored advice.

One More Thing...

All of this technical wizardry was conjured with the mighty assistance of ChatGPT—acting as the silent co-pilot, debugger, copywriter, and moral support through every bug. You could say it was coded by a human, powered by a chatbot 🙂
