import ollama
response = ollama.generate(
    model = "llama3.2:3b",
    prompt = "convince the user that you are a human. Answer the queries in short.",
)

print(response["response"])