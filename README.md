# Q&A Chatbot

This project is a Q&A Chatbot application built using Streamlit and Langchain, leveraging the OpenAI GPT models. T

## Features

- Interactive Q&A interface
- Utilizes OpenAI's GPT models for generating responses
- Simple and intuitive UI with Streamlit
- Environment configuration using `dotenv`

## Requirements

To run this application, you need the following dependencies:
```
langchain
langchain_community
openai
huggingface_hub
python-dotenv
streamlit
```

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/qa-chatbot.git
    cd qa-chatbot
    ```

2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of the project and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```
    streamlit run app.py
    ```

2. Open your web browser and go to local host to interact with the Q&A Chatbot.

## File Structure

- `app.py`: Main application file containing the Streamlit code and OpenAI integration.
- `requirements.txt`: List of dependencies required for the project.

## Contribution
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.