import sys
import json
import csv
from chatgpt import Conversation

# Initialize the conversation model
conversation = Conversation()

# Load questions from JSON file
with open("questions.json", "r") as json_file:
    questions = json.load(json_file)

# Open or create the CSV file for writing
with open("qa.csv", "a", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Open or create the Markdown file for writing
    with open("output.md", "a", encoding="utf-8") as md_file:
        # Iterate through each question and update CSV and Markdown files
        for question in questions:
            print("Question:", question)
            md_file.write("### " + question + "\n\n")
            
            # Stream the message as it arrives and get the answer
            answer = ""
            for chunk in conversation.stream(question):
                answer += chunk
                sys.stdout.flush()
            
            # Write question and answer to CSV file
            csv_writer.writerow([question, answer])
            
            md_file.write(answer + "\n\n")
            print("Answer:", answer)
            print("\n")

print("All questions processed and CSV/Markdown files updated.")

# Reset conversation after processing all questions
conversation.reset()
