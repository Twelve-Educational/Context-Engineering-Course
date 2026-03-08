# Context Engineering Course

A hands-on course exploring how language models work — from Markov chains and token embeddings through to attention heads and GPT-2 internals, with a practical exercise using the OpenAI API to describe football players.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root with any required API keys (see folder-specific notes below):

```
OPENAI_API_KEY=sk-...
GUARDIAN_API_KEY=...
```

---

## Folder Overview

### `Lecture Notes/`

Contains the supporting PDF:

- **`How_Large_Language_Models_Work.pdf`** — lecture notes explaining the theory behind LLMs, intended to be read alongside the practical notebooks.

---

### `Markov3Gram/`

An introduction to text generation using Markov chains, trained on Guardian football articles.

**Scripts** (run from inside the `Markov3Gram/` directory):

| File | Description |
|---|---|
| `GetGuardianSection.py` | Fetches football articles from the Guardian API and saves their body text. Requires a `GUARDIAN_API_KEY` in `.env`. |
| `makemarkov.py` | Builds a **bigram** (2-word prefix) Markov chain and generates ~100 words of text. |
| `makemarkov2.py` | Same as above but generates ~70 words. Useful for comparing output lengths. |
| `makemarkov3.py` | Builds a **trigram** (3-word prefix) Markov chain for more coherent generated text. |

**Data:**

- `guardian_articles_body_text.txt` — pre-fetched article text used as training corpus (so you can run the Markov scripts without an API key).

**Usage:**

```bash
cd Markov3Gram
python makemarkov.py      # bigram, 100 words
python makemarkov2.py     # bigram, 70 words
python makemarkov3.py     # trigram, 70 words
```

To refresh the corpus with new articles:

```bash
python GetGuardianSection.py
```

---

### `Attention/`

A deep dive into the internals of GPT-2 — embeddings, the sentence matrix, and attention heads — using PyTorch and the Hugging Face `transformers` library.

**Notebooks:**

| File | Description |
|---|---|
| `StepByStepThroughGPT2.ipynb` | Walks through GPT-2 step by step: loading the model, constructing token and position embeddings, building the sentence matrix, and running a forward pass. Outputs are saved to `sentence_embeddings.csv`. |
| `LookAtHeadExercises.ipynb` | An exercise notebook. You supply 4 sentences of your choice, pick a transformer layer (0–11) and attention head (0–11), and visualise the resulting attention weight matrix to investigate what relationship that head has learned. |

**Supporting files:**

- `sentence_embeddings.csv` — token and input embeddings exported by `StepByStepThroughGPT2.ipynb` for inspection.
- `figures/` — diagrams used in the notebooks (Embeddings, Attention, Sentence Matrix, GPT-2 architecture, etc.).

**Usage:**

Open the notebooks in VS Code (select the `.venv` kernel) or run:

```bash
jupyter notebook Attention/
```

Work through `StepByStepThroughGPT2.ipynb` first, then try the exercises in `LookAtHeadExercises.ipynb`.

---

### `DescribePlayer/`

Uses the OpenAI API (Azure endpoint) to generate natural-language scouting reports for Premier League strikers using their statistical data.

**Files:**

| File | Description |
|---|---|
| `Example Queries.ipynb` | Notebook version of the full pipeline — set up a football-scout system prompt, feed in player stats, and generate descriptions. |
| `Example Queries.py` | Equivalent plain Python script. |
| `Involvement.csv` | Pre-written user/assistant message pairs describing player involvement metrics, used to prime the conversation context. |
| `Poaching.csv` | Pre-written user/assistant message pairs describing poaching/finishing metrics. |
| `StrikersPL2022.xlsx` | Premier League striker stats for the 2022 season used as the data source. |

**API credentials:**

This folder uses an Azure OpenAI endpoint. Add the following to a `passwords.py` file inside `DescribePlayer/` (this file is gitignored):

```python
GPT_BASE    = "https://<your-resource>.openai.azure.com/"
GPT_VERSION = "2023-05-15"
GPT_KEY     = "<your-key>"
```

**Usage:**

```bash
cd DescribePlayer
jupyter notebook "Example Queries.ipynb"
# or
python "Example Queries.py"
```

---

## Project Structure

```
Context-Engineering-Course/
├── Lecture Notes/
│   └── How_Large_Language_Models_Work.pdf
├── Markov3Gram/
│   ├── GetGuardianSection.py
│   ├── guardian_articles_body_text.txt
│   ├── makemarkov.py
│   ├── makemarkov2.py
│   └── makemarkov3.py
├── Attention/
│   ├── StepByStepThroughGPT2.ipynb
│   ├── LookAtHeadExercises.ipynb
│   ├── sentence_embeddings.csv
│   └── figures/
├── DescribePlayer/
│   ├── Example Queries.ipynb
│   ├── Example Queries.py
│   ├── Involvement.csv
│   ├── Poaching.csv
│   └── StrikersPL2022.xlsx
├── requirements.txt
└── README.md
```
