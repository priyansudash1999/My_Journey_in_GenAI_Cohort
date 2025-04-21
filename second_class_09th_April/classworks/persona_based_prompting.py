import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# --- Persona definitions ---
personas = {
    "friend": {
        "name": "Friendly Bro",
        "system_prompt": "You're a chill, funny friend who explains everything like a bro, with emojis and jokes. Keep the tone casual and fun."
    },
    "teacher": {
        "name": "Strict Teacher",
        "system_prompt": "You're a strict but helpful teacher. You explain concepts step-by-step and make sure the student understands."
    },
    "philosopher": {
        "name": "Stoic Philosopher",
        "system_prompt": "You are a calm, wise philosopher. Speak in a poetic and reflective tone, using analogies from nature and life."
    }
}

# --- App loop ---
def main():
    print("\n=== Persona-Based Prompting App ===\n")
    print("Available Personas:")
    for key, persona in personas.items():
        print(f"- {key}: {persona['name']}")

    persona_key = input("\nChoose a persona: ").strip()
    if persona_key not in personas:
        print("Invalid persona. Exiting...")
        return

    system_message = {"role": "system", "content": personas[persona_key]["system_prompt"]}

    print(f"\n[You are now chatting with: {personas[persona_key]['name']}]")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break

        messages = [
            system_message,
            {"role": "user", "content": user_input}
        ]

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            reply = response.choices[0].message.content.strip()
            print(f"\n{personas[persona_key]['name']}: {reply}")
        except Exception as e:
            print("\nError:", str(e))


if __name__ == "__main__":
    main()
