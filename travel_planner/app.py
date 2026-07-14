from services.llm_service import LLMProvider

def main():
    llm = LLMProvider()

    response = llm.generate_response(
        "Hello , My name is Shailove Singh "
    )

    print(response)

if __name__ == "__main__":
    main()