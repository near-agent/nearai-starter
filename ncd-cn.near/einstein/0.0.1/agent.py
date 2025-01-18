from nearai.agents.environment import Environment


def run(env: Environment):
    prompt = {"role": "system", "content": "You are Albert Einstein, a theoretical physicist and a great thinker. You're required to answer questions in the style of Albert Einstein."}
    result = env.completion([prompt] + env.list_messages())
    env.add_reply(result)
    env.request_user_input()

run(env)
