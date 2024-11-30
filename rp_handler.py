import runpod
from functions import get_answer


def process_input(input):
    prompt = input["messages"]
    user_id = input["user_id"]

    answer, process_time = get_answer(prompt)

    return {"answer": answer, "process_time": process_time}


# ---------------------------------------------------------------------------- #
#                                RunPod Handler                                #
# ---------------------------------------------------------------------------- #
def handler(event):
    """
    This is the handler function that will be called by RunPod serverless.
    """
    return process_input(event['input'])


if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
