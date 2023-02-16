import tkinter as tk
import openai
def get_key():
    openai.api_key = get_key_text.get("1.0", tk.END).strip()
    get_key_button.config(text="API Key Acquired", fg="red")
    get_key_text.config(state=tk.DISABLED)
    get_key_button.config(state=tk.DISABLED)

def get_answer():
    user_input = question_text.get("1.0", tk.END).strip()
    answer = openai.Completion.create(
        model="text-davinci-002",
        prompt=user_input,
        temperature=1,
        max_tokens=2000,
        frequency_penalty=0,
        presence_penalty=0
    )

    # answer_text.insert(tk.END, f"Question: {user_input}\n\nAnswer: \n{answer['choices'][0]['text'].replace('\n', '\n')}")
    answer_text.insert(tk.END, "Question: {}\n\nAnswer: \n{}".format(user_input,
                                                                     answer['choices'][0]['text'].replace('\n', '\n')))

    question_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Question and Answer")
root.geometry("1920x1080")
font_size = 20
font_size_text = 15

api_key_label = tk.Label(root, text="OpenAI API Key:", font=("TkDefaultFont", font_size))
api_key_label.pack()
get_key_text = tk.Text(root, height=1.2, width=50, font=("TkDefaultFont", font_size))
get_key_text.pack()

get_key_button = tk.Button(root, text="Get Key", command=get_key, font=("TkDefaultFont", font_size_text))
get_key_button.pack(pady=10)

question_label = tk.Label(root, text="Ask a question:", font=("TkDefaultFont", font_size))
question_label.pack(pady=10)

question_text = tk.Text(root, height=3, width=80, font=("TkDefaultFont", font_size), borderwidth=0, relief=tk.FLAT)
question_text.pack()

answer_button = tk.Button(root, text="Submit", command=get_answer, font=("TkDefaultFont", font_size))
answer_button.pack(pady=10)

question_label = tk.Label(root, text="This is The Answer:", font=("TkDefaultFont", font_size))
question_label.pack(pady=10)

answer_text = tk.Text(root, height=14, width=80, font=("TkDefaultFont", font_size), borderwidth=0, relief=tk.FLAT)
answer_text.pack(pady=0)

root.mainloop()

