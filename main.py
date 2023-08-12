import sys
import json
import csv
from chatgpt import Conversation

# Initialize the conversation model
conversation = Conversation()

# Load questions from JSON file
with open("questions.json", "r") as json_file:
    questions = json.load(json_file)

# Iterate through each question and update CSV file
for question in questions:
    print("Question:", question)
    
    # Stream the message as it arrives and get the answer
    answer = ""
    for chunk in conversation.stream(question):
        answer += chunk
        sys.stdout.flush()
    
    # Update CSV file with question and answer
    with open("qa.csv", "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([question, answer])
    
    print("Answer:", answer)
    print("\n")

print("All questions processed and CSV updated.")

# Reset conversation after processing all questions
conversation.reset()
