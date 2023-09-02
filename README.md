# Langtrain Chatbot with OpenAI GPT and PDF Query

This Python project, developed for language understanding and question-answering tasks, combines the power of the Langtrain library, OpenAI GPT, and PDF search capabilities. The chatbot leverages these technologies to provide intelligent responses to user queries.

## Project Components

### Langtrain Library
The Langtrain library forms the core of this project, enabling text processing, text splitting, and vector storage for efficient search and retrieval.

### OpenAI GPT
OpenAI GPT (Generative Pre-trained Transformer) is integrated into the chatbot for language understanding and generation. It allows the chatbot to comprehend user queries and generate contextually relevant responses.

### PDF Query
The project includes functionality to extract and search information from PDF documents. It utilizes PyPDF2 to read PDF content and character-based text splitting to segment the text effectively. PDF content is then indexed and made searchable for question-answering.

## Project Workflow

1. **PDF Data Extraction**: The chatbot extracts text data from a specified PDF file.

2. **Text Splitting**: The extracted text is split into manageable chunks for efficient processing.

3. **OpenAI Embeddings**: OpenAI embeddings are employed to encode and understand the textual content.

4. **Vector Search**: The project utilizes vector search technology to index and search the PDF content for relevant information.

5. **Question-Answering Chain**: A question-answering chain is created, incorporating OpenAI's language model to process user queries and provide answers based on the indexed PDF content.

## Usage

The `query(usrtxt)` function within the source code allows users to interact with the chatbot. Simply provide your question as input, and the chatbot will retrieve relevant information from the PDF document and generate responses.

## Flask App with HTML Front End

To facilitate user interaction, this project includes a Flask web application with an HTML-based front-end. Users can input their questions through the web interface and receive real-time responses from the chatbot.

## Getting Started

1. Ensure you have the required dependencies and libraries installed.

2. Set your OpenAI API key as an environment variable.

3. Load a PDF document for the chatbot to query.

4. Run the Flask app to start interacting with the chatbot.

## Contribution

Contributions and improvements to this project are welcome. Feel free to fork the repository, make enhancements, and submit pull requests.



---
*Note: Ensure that your OpenAI API key is correctly configured before using this project.*

