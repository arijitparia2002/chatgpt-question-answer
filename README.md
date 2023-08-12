# ChatGPT Question-Answer Generator

A simple Python script that uses the OpenAI GPT model to answer questions provided in a JSON file and updates a CSV file with the questions and their corresponding answers.

## Installation

To use this script, you'll need the `chatgpt` package. You can install it using pip:

```bash
pip install -U chatgpt
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/arijitparia2002/chatgpt-question-answer.git
cd chatgpt-question-answer
```

2. Create a JSON file named `questions.json` in the project directory. Add your questions to this file in a list format, like so:

```json
[
    "What is the capital of France?",
    "Explain the theory of relativity.",
    "How does photosynthesis work?",
    "Tell me about the history of the Roman Empire.",
    "What are the benefits of regular exercise?"
]
```

3. Run the script to process the questions and generate answers:

```bash
python answer_questions.py
```

The script will process each question, generate answers, and update a CSV file named `qa.csv` in the project directory with the question-answer pairs.

## CSV Format

The CSV file `qa.csv` will have two columns: "Question" and "Answer". Each processed question and its corresponding answer will be added as a new row in the CSV file.

## Markdown Output

In addition to the CSV file, the script will generate a Markdown file named output.md. This file will include the questions as headings (with `###`) and the corresponding answers in formatted text. Each question and answer pair will be separated by a blank line.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

