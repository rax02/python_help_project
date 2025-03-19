## AI agents

key concepts:
- A vector database stores numerical representations (embeddings) of text or other data, created by machine learning models. It enables semantic search by identifying similar meanings in high-dimensional space.

- Multi-agent structures allow to separate memories between different sub-tasks, with two great benefits:
Each agent is more focused on its core task, thus more performant
Separating memories reduces the count of input tokens at each step, thus reducing latency and cost.

- types of agents
    - toolCallingAgents
    - codeAgent

- Agentic RAG

## Langchain (agent interface)
- LangChain provides a standard interface to interact with models and other components, useful for retrieval, LLM calls and tools calls. The classes from LangChain might be used in LangGraph, but do not HAVE to be used.

## Langgraph (agent workflow)
- Code Agents, like the ones you can encounter in smolagents, are very free. They can call multiple tools in a single action step, create their own tools, etc. LangGraph is particularly valuable when you need Control over your applications. It gives you the tools to build an application that follows a predictable process while still leveraging the power of LLMs.

## LangSmith (agent tracing)


