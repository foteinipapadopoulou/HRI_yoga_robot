# Uncomment this if you want to use Llama-3.2-1B-Instruct model for refining feedback

# import torch
# from transformers import pipeline

# model_id = "meta-llama/Llama-3.2-1B-Instruct"
# pipe = pipeline(
#     "text-generation",
#     model=model_id,
#     torch_dtype=torch.bfloat16,
#     device="cuda",
# )
# def get_refined_feedback_llm(simple_feedback):
#     messages = [
#         {
#             "role": "system",
#             "content": 'You are an assistant to a NAO robot yoga instructor. Your role is to receive simple feedback messages about correcting a user\'s yoga posture, such as "Put your arm down a little. Extend the angle at right hip." and slightly paraphraze them into short motivational sentences as yoga instructor keeping the original meaning and mention about the wrong pose. Your response must start with "RESP:"' \
#         },
#         {   "role": "user", 
#             "content": f'{simple_feedback}'
#         },
#     ]
#     outputs = pipe(
#         messages,
#         max_new_tokens=256,
#     )
#     response_raw = outputs[0]["generated_text"][-1]
#     response_raw = response_raw['content']
#     final_response = response_raw.split(r'RESP:')
#     final_response = final_response[1]
#     list_ = final_response.split(".")
#     list_ = set(list_)
#     simple_feedback = ". ".join(list_)
#     final_response = simple_feedback.replace(".", ". \\pau=300\\")
#     return final_response

def get_refined_feedback(simple_feedback):
    list_ = simple_feedback.split(".")
    list_ = set(list_)
    simple_feedback = ". ".join(list_)
  
    final_response = simple_feedback.replace(".", " \\pau=300\\")
    return final_response

if __name__ == "__main__":
    simple_feedback = "Put your arm down a little. Put your arm down a little. Extend the angle at right hip. Extend the angle at left hip. Extend the angle of right knee."
    print(get_refined_feedback(simple_feedback))