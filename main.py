import sys

from llm_client import get_response
from prompts import SYSTEM_PROMPT

sys.stdout.reconfigure(encoding="utf-8")

EXIT_COMMANDS = {"exit", "quit"}


def main():
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    print("İngilizce Konuşma Pratiği Botu — çıkmak için 'exit' veya 'quit' yazın.\n")

    while True:
        try:
            user_input = input("Sen: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGörüşürüz!")
            break

        if not user_input:
            continue
        if user_input.lower() in EXIT_COMMANDS:
            print("Görüşürüz!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            reply = get_response(messages)
        except Exception as e:
            print(f"Bir hata oluştu, tekrar dener misin?: {e}\n")
            messages.pop()
            continue

        print(f"Bot: {reply}\n")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
