
# AI Financial Advisor and Web Researcher

This project features an AI-powered system designed for financial advising and web research. The system uses the **Groq** model and integrates with various tools such as **YFinance** for financial data and **DuckDuckGo** for web research. It is built using the **Phi** framework, **FastAPI**, and **Streamlit**.

## Project Structure

1. **playground.py**: Main file that initializes the agents and serves the Playground app.
2. **financial_advisor.py**: A script that defines the financial advisor agent and web researcher agent. These agents perform financial analysis and gather web data respectively.
3. **.env**: Stores environment variables, particularly the API key for Groq.

## Features

- **Financial Advisor Agent**:
    - Provides stock prices, analyst recommendations, and stock fundamentals using **YFinance**.
    - Allows easy querying of financial data in table format.
    - Uses an SQLite database to store data from interactions.

- **Web Researcher Agent**:
    - Uses **DuckDuckGo** to fetch information from the web.
    - Always includes the source of the data retrieved.

- **Agent Team**:
    - Combines the financial advisor and web researcher agents into a team, allowing for integrated financial and web research tasks.

## Prerequisites

Before running the project, make sure you have the following dependencies installed:

- Python 3.x
- **Phi** library (for Groq models and agents)
- **dotenv** for managing environment variables
- **SQLite** for storing agent interaction history
- **YFinance** for financial tools
- **DuckDuckGo** for web research

You can install these dependencies using `pip`:

```bash
pip install phi dotenv yfinance duckduckgo
```

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/ai-financial-advisor.git
    cd ai-financial-advisor
    ```

2. Create a `.env` file in the root directory and add your **GROQ_API_KEY**:

    ```ini
    GROQ_API_KEY=your_api_key_here
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the Playground app with the agents, execute the following command:

```bash
python playground.py
```

The app will start and you can interact with both agents through the user interface.

## How It Works

- **Playground**: The Playground app combines the financial advisor and web researcher agents. The `financial_advisor` agent handles financial data retrieval and analysis, while the `web_researcher` agent is responsible for pulling relevant web data. 
- **SQL Storage**: Both agents store their interaction history in an SQLite database for later retrieval and analysis.

## Example Use Case

You can ask the agents questions like:

- "Is NTPC stock a good buy?"
- "What are the latest analyst recommendations for Apple?"
- "Find the latest news on the solar energy market."

The agents will fetch the required data and present it in a user-friendly format, including tables for financial data and sources for web research.

## Contributing

Contributions are welcome! If you'd like to contribute, feel free to open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
