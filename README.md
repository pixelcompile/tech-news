# Tech News API

This project is a FastAPI application that provides endpoints to fetch IT news stories using two different AI models: OpenAI and Gemini.

## Project Structure

```
tech-news-api
├── src
│   ├── main.py               # Entry point of the FastAPI application
│   ├── openai_tech.py        # Logic for interacting with the OpenAI API
│   ├── gemini_tech.py        # Logic for interacting with the Gemini API
│   └── routes
│       ├── openai_route.py   # FastAPI route for OpenAI
│       └── gemini_route.py    # FastAPI route for Gemini
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd tech-news-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

## Usage

To run the FastAPI application, execute the following command:

```bash
uvicorn src.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- **OpenAI IT News**
  - **GET** `/openai/news`
  - Description: Fetches IT news stories using the OpenAI API.

- **Gemini IT News**
  - **GET** `/gemini/news`
  - Description: Fetches IT news stories using the Gemini API.

## License

This project is licensed under the MIT License.