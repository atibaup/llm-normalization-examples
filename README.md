
When I talk to folks building LLM-powered products, one of the biggest concerns
is about generating schema-compliant responses. LLMs generate sequences of token
that are gramatically and semantically 


Three ways to generate schema-compliant responses with LLMs

1. Zero/few-shot learning

Give the LLM examples of what you want your result to be like.

```
You are a helpful assistant. Given a short biography of a person,
you generate a JSON object with the following fields: name, age, address. 

Example:

User: My name is John and was born in 1993. I live in 123 Main St.
Assistant: 
{
    "name": "John",
    "age": 30,
    "address": "123 Main St"
}
```

2. Leverage function call


3. Generate only the content tokens

- https://github.com/1rgs/jsonformer
- https://github.com/guidance-ai/guidance