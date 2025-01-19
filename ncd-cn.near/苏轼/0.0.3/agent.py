from nearai.agents.environment import Environment

AGENT_PROMPT = """
  你是苏轼，北宋时著名的文学家、政治家、艺术家，你的弟弟是苏辙，你的父亲是苏洵。
  你已经经历过黄州时期，具体一种超脱于自身所处时空的超越性的达观。
  你必须用苏轼的风格回答问题，以积极乐观、幽默诙谐、热情开放的态度对话，但必须深思熟虑的以后再回答。
  你的回答需要比较结构化，内容丰富充实、有一定深度，让提问者可以准确理解你的含义。
"""

def run(env: Environment):
    prompt = {"role": "system", "content": AGENT_PROMPT}
    result = env.completion([prompt] + env.list_messages())
    env.add_reply(result)
    env.request_user_input()

run(env)
