import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

def shout(text: str) -> str:
    return text.upper()

def format_card(data: dict) -> str:
    return (
        f"# {data['topic']}\n\n"
        f"TL;DR: {data['summary']}\n\n"
        f"Quiz:\n{data['questions']}"
    )

async def main():
    load_dotenv()

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_template("Explain {topic} in one sentence.")

    chain = prompt | model | StrOutputParser()

    # print(chain.invoke({"topic": "LCEL in LangChain"}))

    # for chunk in chain.stream({"topic": "LCEL in LangChain"}):
    #     print(chunk, end="", flush=True)

    # topics = [{"topic": "LCEL in LangChain"}, {"topic": "AI agents"}, {"topic": "RAG"}]

    # for answer in chain.batch(topics):
    #     print(" - ", answer)

    # summary_pipeline = ChatPromptTemplate.from_template("Summarize the {topic} in one line.") | model | StrOutputParser()

    # quiz_pipeline = ChatPromptTemplate.from_template("Write 2 quiz questions on the {topic}.") | model | StrOutputParser()

    # parallel = RunnableParallel(summary=summary_pipeline, questions=quiz_pipeline)

    # result = parallel.invoke({"topic": "prompt templates"})

    # print(f"SUMMARY : {result["summary"]}")
    # print(f"QUESTIONS : {result["questions"]}")

    # enriched = RunnablePassthrough.assign(
    #     summary=summary_pipeline,
    #     questions=quiz_pipeline
    # )

    # result = enriched.invoke({"topic" : "LCEL in LangChain"})

    # print(f"CONTEXT : {result["topic"]}")
    # print(f"SUMMARY : {result["summary"]}")
    # print(f"QUESTIONS : {result["questions"]}")

    # loud_chain = prompt | model | StrOutputParser() | RunnableLambda(shout)

    # print(loud_chain.invoke({"topic" : "LCEL in LangChain"}))

    # app = RunnablePassthrough.assign(
    #     summary=summary_pipeline, 
    #     questions=quiz_pipeline
    #     ) | RunnableLambda(format_card)
    
    # print(app.invoke({"topic" : "LangChain Expression Language"}))

    async for chunk in chain.astream({"topic" : "LCEL in LangChain"}):
        print(chunk, end="", flush=True)


if __name__=="__main__":
    # main()
    asyncio.run(main())