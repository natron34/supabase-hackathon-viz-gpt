import openai


openai.organization = ''
openai.api_key = ''

response = openai.Embedding.create(
    input="Cat is to dog as king is to queen",
    model="text-embedding-ada-002"
)
embeddings = response['data'][0]['embedding']
print(openai.Completion.create(model="text-davinci-003", prompt="How are you?", temperature=0, max_tokens=7))