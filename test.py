from rag import ask_question


def main():

    print("=" * 60)
    print("🧠 Local AI Document Assistant")
    print("=" * 60)

    print("Type 'exit' to quit.\n")

    while True:

        question = input("Ask a question: ")

        if question.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break

        try:

            answer, docs = ask_question(question)

            print("\n" + "=" * 60)
            print("Answer")
            print("=" * 60)
            print(answer)

            print("\n" + "=" * 60)
            print("Retrieved Context")
            print("=" * 60)

            for i, doc in enumerate(docs, 1):

                page = doc.metadata.get("page", "Unknown")

                print(f"\nSource {i} | Page {page}")
                print("-" * 60)
                print(doc.page_content)

            print("\n")

        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()