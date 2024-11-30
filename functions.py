import time
import ollama


def get_answer(ipt: list[dict]):

    start_time = time.perf_counter()
    try:
        response = ollama.chat(model='assistant', messages=ipt)
        msg: str = response["message"]["content"]
    except ollama.ResponseError as e:
        return e.error

    end_time = time.perf_counter()
    delta = end_time-start_time

    return msg, delta
