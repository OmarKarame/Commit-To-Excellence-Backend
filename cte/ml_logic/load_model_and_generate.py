from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from transformer import  generate_commit_message, data_source, get_data, create_t5_model

# TOKENIZER IS NOT WORKING CORRECTLY!
#path to model will need to be changed as is currently being saved outside of the project files(still uploaded on the main branch for now)
choice = int(input("Pick data point:"))
model = AutoModelForSeq2SeqLM.from_pretrained("saved_models/t5-small-cte")
tokenizer1 = AutoTokenizer.from_pretrained("saved_models/t5-small-cte")


print("model loaded")
basic_model = create_t5_model()
print("basic model loaded")

data = get_data(data_source)
print("data loaded)")

comment = generate_commit_message(data["diff"].iloc[choice], model, tokenizer1)
print("predicted comment")
print(comment)
print(f"\n")

basic_comment = generate_commit_message(data["diff"][choice], basic_model, tokenizer1)
print("predicted basic comment")
print(basic_comment)
print(f"\n")

print("actual comment")
print(data["message"][choice])
