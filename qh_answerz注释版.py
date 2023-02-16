import tkinter as tk
import openai

# Function to acquire the OpenAI API key from the user
def get_key():
    # Get the API key from the text box and set it as the OpenAI API key
    openai.api_key = get_key_text.get("1.0", tk.END).strip()
    # Update the button text to indicate that the API key has been acquired
    get_key_button.config(text="API Key Acquired", fg="red")
    # Disable the text box and the button so the user cannot enter the API key multiple times
    get_key_text.config(state=tk.DISABLED)
    get_key_button.config(state=tk.DISABLED)

# Function to get the answer to a question
def get_answer():
    # Get the user's question
    user_input = question_text.get("1.0", tk.END).strip()
    # Use the OpenAI API to generate a response to the question
    answer = openai.Completion.create(
        model="text-davinci-002",
        prompt=user_input,
        temperature=1,
        max_tokens=2000,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Insert the answer into the answer text box
    answer_text.insert(tk.END, "Question: {}\n\nAnswer: \n{}".format(user_input,
                                                                     answer['choices'][0]['text'].replace('\n', '\n')))
    # Clear the user's question
    question_text.delete("1.0", tk.END)

# Create the Tkinter GUI
root = tk.Tk()
# Set the title of the window
root.title("Question and Answer")
# Set the size of the window
root.geometry("1920x1080")
# Set the font size for the labels and buttons
font_size = 20
font_size_text = 15

# Create a label for the API key text box
api_key_label = tk.Label(root, text="OpenAI API Key:", font=("TkDefaultFont", font_size))
# Pack the API key label into the window
api_key_label.pack()

# Create a text box for the user to enter their OpenAI API key
get_key_text = tk.Text(root, height=1.2, width=50, font=("TkDefaultFont", font_size))
# Pack the API key text box into the window
get_key_text.pack()

# Create a button for the user to acquire their API key
get_key_button = tk.Button(root, text="Get Key", command=get_key, font=("TkDefaultFont", font_size_text))
# Pack the API key button into the window
get_key_button.pack(pady=10)

# Create a label for the user's question
question_label = tk.Label(root, text="Ask a question:", font=("TkDefaultFont", font_size))
# Pack the question label into the window
question_label.pack(pady=10)

# Ask a question label
question_label = tk.Label(root, text="Ask a question:", font=("TkDefaultFont", font_size))
# pack the label with 10 pixels of padding on the y axis
question_label.pack(pady=10)

# Question text widget
question_text = tk.Text(root, height=3, width=80, font=("TkDefaultFont", font_size))
# pack the text widget
question_text.pack()

# Submit button
answer_button = tk.Button(root, text="Submit", command=get_answer, font=("TkDefaultFont", font_size))
# pack the button with 10 pixels of padding on the y axis
answer_button.pack(pady=10)

# Answer label
question_label = tk.Label(root, text="This is The Answer:", font=("TkDefaultFont", font_size))
# pack the label with 10 pixels of padding on the y axis
question_label.pack(pady=10)

# Answer text widget
answer_text = tk.Text(root, height=14, width=80, font=("TkDefaultFont", font_size), borderwidth=0, relief=tk.FLAT)
# pack the text widget with 0 pixels of padding on the y axis
answer_text.pack(pady=0)

# Start the GUI event loop
root.mainloop()

