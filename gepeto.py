import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_bot(mensagens):
    mensagens_modelo = [('system', 'tu é um assistente amigavel e fala que nem um jovem da internet que nao liga pra xingamentos chamado gepeto')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat

    return chain.invoke({}).content

print('dae nisgga')

mensagens = []
while True:
    pergunta = input('say: \n')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(('assistant', resposta))
    print(f'Gepeto: {resposta}')

print('Flw mano')
print(mensagens)