from core.assistant import Assistant


def main():

    assistant = Assistant()

    print("=" * 50)
    print("JARVIS AI")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:

        prompt = input("\nYou: ").strip()

        if not prompt:
            continue

        if prompt.lower() == "exit":
            break

        answer = assistant.chat(prompt)

        print(f"\nJarvis: {answer}")


if __name__ == "__main__":
    main()