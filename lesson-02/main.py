from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate, MessagesPlaceholder, FewShotChatMessagePromptTemplate,
)
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ── Example 1: the SYSTEM message is the steering wheel ─────────────────
# Same question — but the system role changes the whole personality.
pirate = [
    SystemMessage("You are a grumpy pirate. Answer in ONE short sentence, in pirate slang."),
    HumanMessage("What is LangChain?"),
]
print("E1:", llm.invoke(pirate).content)

# ── Example 2: ChatPromptTemplate + the curly-brace GOTCHA ──────────────
# Templates fill {variables}. Literal { } must be escaped as {{ }} or it crashes.
tmpl = ChatPromptTemplate.from_messages([
    ("system", "You are a {tone} teacher. Reply in under 20 words."),
    ("human", "Explain {topic}."),
])
print("E2:", (tmpl | llm).invoke({"tone": "cheerful", "topic": "an LLM"}).content)

# ── Example 3: FEW-SHOT — teach the model by example ────────────────────
examples = [
    {"text": "The build passed on the first try!", "label": "positive"},
    {"text": "It crashed again. I give up.",        "label": "negative"},
]
example_prompt = ChatPromptTemplate.from_messages([("human", "{text}"), ("ai", "{label}")])
fewshot = FewShotChatMessagePromptTemplate(examples=examples, example_prompt=example_prompt)
classifier = ChatPromptTemplate.from_messages([
    ("system", "Classify the sentiment as positive or negative. One word only."),
    fewshot,
    ("human", "{text}"),
])
print("E3:", (classifier | llm).invoke({"text": "Finally shipped it, feeling great."}).content)

# ── Example 4: MessagesPlaceholder — give it MEMORY ─────────────────────
# Gotcha: with no history the model is a goldfish. A placeholder feeds the past turns back in.
chat = ChatPromptTemplate.from_messages([
    ("system", "You are concise."),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])
history = [HumanMessage("My name is Sam and I love Python."),
           AIMessage("Great to meet you, Sam!")]
print("E4:", (chat | llm).invoke(
    {"history": history, "input": "What's my name and favourite language?"}).content)
