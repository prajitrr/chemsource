from openai import OpenAI

def classify(name,
             input_text=None, 
             api_key=None, 
             baseprompt=None,
             model='gpt-4-0125-preview', 
             temperature=0,
             top_p = 0,
             logprobs=None,
             max_length=250000):
    
    if model == "deepseek-chat":
        client = OpenAI(
                        api_key=api_key,
                        base_url="https://api.deepseek.com"
                        )

    else:
        client = OpenAI(
                        api_key=api_key
                        )

    split_base = baseprompt.split("COMPOUND_NAME")
    prompt = split_base[0] + str(name) + split_base[1] + str(input_text)
    prompt = prompt[:max_length]

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
        temperature=temperature,
        top_p=top_p,
        logprobs=logprobs,
        stream=False
        )
    
    if logprobs:
        return response.choices[0].message.content, response.choices[0].logprobs
    else:
        return response.choices[0].message.content