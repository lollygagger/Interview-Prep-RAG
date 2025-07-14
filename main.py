import RAG

def main():
    print("Setting up your local Amazon prep assistant...")
    split_docs = RAG.load_and_split_pdfs("./pdfs")
    vectorstore = RAG.embed_documents(split_docs)
    rag_chain = RAG.setup_rag_chain(vectorstore)

    print("\n✅ Ready! Ask anything about your prep docs. Type 'exit' to quit.")
    while True:
        query = input("\n🧠 You: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = rag_chain.invoke(query)
        print(f"\n🤖 Bot: {response['result']}")

if __name__ == "__main__":
    main()