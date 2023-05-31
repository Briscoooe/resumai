from langchain.llms import OpenAI
from langchain.chains import ConversationChain

# llm = OpenAI(openai_api_key=os.environ['OPENAI_API_KEY'])

# prompt = PromptTemplate(
#     input_variables=["product"],
#     template="What is a good name for a company that makes {product}?",
# )
#
#
# chain = LLMChain(
#     prompt=prompt,
#     llm=llm
# )
# print(chain.run("colorful socks"))

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.predict(input="Hi there!")
print(output)
output = conversation.predict(
    input="I'm doing well! Just having a conversation with an AI."
)
print(output)
