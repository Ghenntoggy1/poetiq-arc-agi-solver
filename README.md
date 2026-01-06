# [Poetiq](https://poetiq.ai): SOTA Reasoning on ARC-AGI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/Package%20Manager-uv-purple)](https://docs.astral.sh/uv/getting-started/installation/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-green)](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)
[![Conventional Branch](https://img.shields.io/badge/Conventional%20Branch-Spec-6192c3)](https://conventional-branch.github.io/)
[![ARC-AGI](https://img.shields.io/badge/Task-ARC--AGI-red)](https://arcprize.org/)

This repository allows reproduction of **Poetiq's** record-breaking submission to the ARC-AGI-1 and ARC-AGI-2 benchmarks.

Full analysis is available in our launch post, **[Traversing the Frontier of Superintelligence](https://poetiq.ai/posts/arcagi_announcement/)**.

Our method is now on top of the official leaderboard. More information is in our follow-up post, **[Poetiq Shatters ARC-AGI-2 State of the Art at Half the Cost](https://poetiq.ai/posts/arcagi_verified/)**.

---

## 📊 Public Eval Results

You can recreate the Gemini 3 points from these charts using this repo.

<p align="center">
  <img alt="ARC-AGI-1 Public Eval Score" src=".assets/images/arcagi1.png" width="45%" />
  <img alt="ARC-AGI-2 Public Eval Score" src=".assets/images/arcagi2.png" width="45%" />
</p>

## 📊 Official Private Eval Results

These are our results on the official leaderboard from ARC Prize, but those problems are kept private.

<p align="center">
  <img alt="ARC-Prize Official Table" src=".assets/images/officialtable_boxed.png" width="755%" />
</p>
<p align="center">
  <img alt="ARC-AGI-2 Semi-Private Score" src=".assets/images/arc2captured.png" width="60%" />
</p>

## 🛠️ Usage

### Prerequisites

- Python 3.11+
- `uv` package manager (optional)
- API Keys for the models you wish to test (Gemini, OpenAI, OpenRouter, etc.)

### Quick Start

1. Setup the environment:
    - using python:

    ```sh
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

    - using `uv`:

    ```sh
    uv venv .venv -p <your-python-version>
    source .venv/bin/activate # Linux
    .\.venv\Scripts\activate.ps1 # Windows
    ```

2. Install the dependencies:
    - using `pip`:

    ```sh
    pip install .\.requirements\requirements-original.txt
    ```

    - using `uv`:

    ```sh
    uv sync
    ```

3. Create a .env file in the root directory. You must include keys for the models you intend to run.

    ```bash
    GEMINI_API_KEY=...
    OPENAI_API_KEY=...
    OPENROUTER_API_KEY=...
    ```

4. Modify the constants in main.py to set the problem set, number of problems, etc. Then run the script:

    ```bash
    python main.py
    ```

5. By default, the code runs the Poetiq 3 config described in the blog post. You can uncomment other ones or modify the config in config.py

## 📄 Contact

If you use this code or these results in your research, please cite our blog post:

Poetiq Team. (2025). *Traversing the Frontier of Superintelligence*. Poetiq AI. [https://poetiq.ai/posts/arcagi_announcement/](https://poetiq.ai/posts/arcagi_announcement/)

For questions or to discuss the future of reasoning, reach out to us at <poetiq@poetiq.ai>.

[![X (formerly Twitter)](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/poetiq_ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/poetiq/)
[![Bluesky](https://img.shields.io/badge/Bluesky-0285FF?style=for-the-badge&logo=Bluesky&logoColor=white)](https://bsky.app/profile/poetiq-ai.bsky.social)
