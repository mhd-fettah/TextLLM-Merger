# TextLLM Merger

**TextLLM Batcher** is a local-first AI text batch processing tool designed to work with any large language model (LLM). The tool enables automated analysis and information extraction from batches of text files using custom prompts. It is fully prompt-agnostic and can handle a variety of text-processing tasks.

<p align="center">
  <img src="textllm-banner.png" alt="TextLLM Batcher banner" />
</p>

We highly recommend using **LM Studio** in combination with a powerful text model for an efficient and private local inference setup. LM Studio makes it easy to run the model locally with a simple interface and API access. However, the tool is LLM-agnostic—so you're free to integrate any other LLM API that supports text inputs.

## Features

- Batch processes text files using any compatible LLM
- Extracts insights from text based on user-defined prompts
- Tracks processing history with batch IDs
- Organized folder structure and auto-sorting
- Clear logging and error handling
- Progress tracking with visual feedback

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/TextLLM-Batcher.git
```

2. Navigate to the project directory:

```bash
cd TextLLM-Batcher
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

4. Install required packages:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory. Replace the API URL and model name below with your preferred LLM endpoint and model:

```plaintext
LLM_API_URL=http://localhost:1234/v1/chat/completions
LLM_MODEL_NAME=deepseek-r1-distill-qwen-7b
```

## Usage

1. Place your text files in the `input` folder
2. Add your prompt in `prompt.txt` in the root directory
3. Run the application:

```bash
python main.py
```

4. Processed results will be saved in the `output` folder

## Sample Prompts

Customize the prompt to match the kind of analysis you want to perform on the text files. Below are a few useful examples:

### Summarize Text Content
```txt
Summarize the following text in 3-5 sentences, highlighting the key points and main ideas.
```

### Extract Key Information
```txt
Extract all names, dates, locations, and numerical data from the following text.
```

### Sentiment Analysis
```txt
Analyze the sentiment of the following text. Determine if it's positive, negative, or neutral, and explain why.
```

### Content Classification
```txt
Classify the following text into one of these categories: Business, Technology, Health, Education, Entertainment, or Other. Explain your reasoning.
```

### Question Answering
```txt
Based on the following text, answer these questions:
1. What is the main topic?
2. Who are the key individuals mentioned?
3. What are the primary arguments or points made?
```

### Language Translation
```txt
Translate the following text into [target language].
```

### Text Reformatting
```txt
Reformat the following text into a structured bullet-point list organized by topics.
```

### Technical Analysis
```txt
Analyze the following technical document and identify key concepts, methodologies, and potential applications.
```

## Requirements

- Python 3.8+
- An LLM API (e.g., LM Studio with a text model)
- Python packages:
  - requests
  - python-dotenv
  - tqdm

## Contributing

Pull requests are welcome. For major changes, please open an issue to discuss what you want to change first.

## License

[MIT](https://choosealicense.com/licenses/mit/)```

This updated README reflects the project's current focus on text processing rather than image processing. I've updated the title, description, features, usage instructions, and sample prompts to align with text processing capabilities. You may need to create a new banner image (textllm-banner.png) to replace the previous one.
