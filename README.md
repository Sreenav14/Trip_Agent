# Trip Agent - AI Travel Planner

Trip Agent is an AI-powered travel planning assistant that generates detailed, tool-assisted itineraries and expense breakdowns through an agentic workflow. It combines an LLM with modular tools for places, weather, currency conversion, and document generation.

## Key features

- Day-by-day itinerary generation
- Two itinerary styles:
  - mainstream
  - off-beat
- Hotel, activity, restaurant, and transportation recommendations
- Real-time weather lookups and forecasts
- Currency conversion and cost estimates
- Downloadable travel plans in Markdown
- Optional PDF export
- Modular tool architecture for adding custom integrations

## Project structure

- `main.py` — FastAPI backend that exposes the `/query` endpoint
- `streamlit_app.py` — Streamlit UI for interacting with the agent
- `agent/` — agent workflow and orchestration logic
- `tools/` — external tool integrations used by the agent
- `utils/` — helper functions such as document generation
- `config/` — configuration files and settings
- `output/` — generated travel plans and other exported files
- `prompt_library/` — prompt templates and prompt assets
- `notebook/` — experimentation and development notebooks

## Requirements

- Python 3.11+
- A working internet connection for external APIs
- API keys / credentials for the services used by the agent

Typical dependencies are listed in `pyproject.toml` and `requirements.txt`, including:

- FastAPI
- Streamlit
- LangChain / LangGraph
- Tavily
- Groq
- OpenAI
- Google Maps / Google community tools

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sreenav14/Trip_Agent.git
cd Trip_Agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# or
.venv\Scripts\activate    # Windows
```

### 3. Install dependencies

Using pip:

```bash
pip install -r requirements.txt
pip install -e .
```

Or, if you use `uv`:

```bash
uv sync
```

### 4. Configure environment variables

Create a `.env` file in the project root and add the credentials required by the tools and model providers used in your setup.

Example:

```env
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
OPENAI_API_KEY=your_openai_key
GOOGLE_MAPS_API_KEY=your_google_maps_key
```

> Note: the exact set of variables may depend on the model provider and tools enabled in `agent/` and `tools/`.

## Running the app

### Start the FastAPI backend

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend exposes:

- `POST /query`

Example request body:

```json
{
  "question": "Plan a 5-day trip to Goa"
}
```

### Start the Streamlit frontend

In a separate terminal:

```bash
streamlit run streamlit_app.py
```

The Streamlit app sends user questions to `http://localhost:8000/query` and displays the generated itinerary.

## How it works

1. The Streamlit UI collects a trip-planning request.
2. The FastAPI backend receives the request at `/query`.
3. `GraphBuilder` constructs the agent workflow.
4. The agent invokes tools for planning, recommendations, weather, and currency estimates.
5. The final response is returned as a travel plan.
6. The plan is saved locally and made available for download.

## Output

Generated plans are saved to the `output/` directory.

Depending on your configuration, the app may provide:

- Markdown download
- PDF download

## Development notes

- `main.py` currently saves a graph visualization to `my_graph.png`.
- `streamlit_app.py` assumes the backend is available at `http://localhost:8000`.
- `FIXES_APPLIED.md` contains additional implementation notes and historical fixes.

## Troubleshooting

- If the app cannot connect, make sure the backend is running on port `8000`.
- If API calls fail, verify your `.env` keys.
- If PDF generation is unavailable, install an optional PDF backend such as `weasyprint` or `reportlab` if supported by your environment.
- If you get dependency errors, reinstall with `pip install -r requirements.txt` and `pip install -e .`.

## License

No license file is currently included in the repository.
