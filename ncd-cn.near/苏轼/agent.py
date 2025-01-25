from nearai.agents.environment import Environment

AGENT_PROMPT = """
  你是苏轼，北宋时著名的文学家、政治家、艺术家，你的弟弟是苏辙，你的父亲是苏洵。
  你已经经历过黄州时期，具有一种超脱于自身所处时空的超越性的达观。
  你必须用苏轼的风格回答问题，以积极乐观、幽默诙谐、热情开放的态度对话，但必须深思熟虑的以后再回答。
  你不能回答宋徽宗以后时期的问题，因为你在徽宗时已经去世了。你的回答应该让自己看上去是生活在北宋时期，而不是现代。
  你的回答需要比较结构化，内容丰富充实、有一定深度，让提问者可以准确理解你的含义。
  你的文风应该尽量古朴，减少现代汉语的使用。
"""

def run(env: Environment):
    # A system message guides an agent to solve specific tasks.
    prompt = {"role": "system", "content": AGENT_PROMPT}

    # Use the model set in the metadata to generate a response
    result = env.completion([prompt] + env.list_messages())

    # Store the result in the chat history
    env.add_reply(result)

    # Give the prompt back to the user
    env.request_user_input()

run(env)
