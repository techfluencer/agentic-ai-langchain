from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1) a model
llm = ChatOpenAI(model="gpt-4o-mini")
print(llm.invoke("In one sentence, what is LangChain?").content)

# 2) a prompt template
prompt = ChatPromptTemplate.from_template(
    "You are a witty teacher. Explain {topic} to a beginner in 2 short sentences."
)

# 3) chain them with LCEL:  prompt | model | parser
chain = prompt | llm | StrOutputParser()
print(chain.invoke({"topic": "LangChain"}))
print(chain.invoke({"topic": "an AI agent"}))
