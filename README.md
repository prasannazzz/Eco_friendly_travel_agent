
#  Eco-Friendly Trip Recommender

> An intelligent travel planning application that leverages **Google Gemini (LLM)** and **LangChain** to create customized, sustainable travel itineraries. Built with **Streamlit**, this tool supports eco-conscious travelers by offering optimized, low-emission trip plans with estimated carbon footprints.

---

## What Sets This Project Apart

 **LLM + LangChain Agent Framework**  
Built on top of **LangChain**, this project uses a Gemini-based agent to dynamically generate rich, context-aware itineraries based on user preferences — including sustainability goals.

 **Eco Mode Personalization**  
Unlike traditional travel planners, this tool includes a toggle for **eco-friendly trip planning**, altering suggestions to:
- Prefer train/bus travel
- Recommend vegetarian/vegan dining
- Highlight eco-certified accommodations
- Estimate and display carbon emissions

 **Modular Architecture**  
Uses a clean separation of concerns:
- Prompt templates
- Carbon emission estimation utilities
- LLM agent pipeline
- Streamlit UI layer

 **Mock CO₂ Estimation**  
Includes a utility to approximate emissions based on transportation mode, helping raise awareness of travel impact.


##  Tech Stack

| Layer              | Technology                         |
|-------------------|-------------------------------------|
| **Frontend**       | Streamlit                          |
| **LLM Provider**   | Google Gemini (`gemini-pro`)       |
| **Agent Framework**| LangChain                          |
| **Prompt Design**  | `PromptTemplate` (Jinja-style)     |
| **Environment**    | Python 3.10, Pipenv                |
| **CO₂ Logic**      | Custom utility with emission factors |


##  Project Structure



eco\_trip\_planner/
├── main.py                   # Streamlit application
├── .env                      # Gemini API key
├── Pipfile                   # Dependency definitions
├── agents/
│   └── eco\_agent.py          # LangChain LLM agent logic
├── prompts/
│   └── eco\_prompt.txt        # Dynamic prompt template
├── utils/
│   └── carbon\_utils.py       # CO₂ footprint estimator





## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/eco-trip-planner.git
cd eco-trip-planner
````

### 2. Add API Key to `.env`

```env
GOOGLE_API_KEY=your-gemini-api-key
```

> Get your Gemini key here: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

### 3. Install Dependencies

```bash
pipenv install
pipenv shell
```

### 4. Run the App

```bash
streamlit run main.py
```

Open in your browser at `http://localhost:8501`.

---

## 🔍 Core Functionality

| Feature                         | Description                                           |
| ------------------------------- | ----------------------------------------------------- |
| **Gemini LLM Planning**         | Generates smart travel plans using structured prompts |
| **Eco Mode**                    | Alters trip generation logic for sustainability       |
| **Carbon Footprint Estimation** | Calculates kg of CO₂ based on transportation choices  |
| **LangChain PromptTemplate**    | Modular and dynamic prompting system                  |
| **Interactive Streamlit UI**    | Input-based personalization with live feedback        |

---

##  Sample Use Case

**Scenario**:

> A user wants to plan a trip from Pune to Shimla, prefers vegetarian food, has a budget of \$500, and wants to minimize carbon emissions.

**Result**:

* Suggests overnight trains instead of flights
* Recommends eco-friendly lodges
* Lists vegetarian restaurants
* Outputs estimated carbon emissions (\~40kg CO₂)

---


## Contributing

We welcome contributions in:

* Emission modeling
* LangChain integrations
* UI design and responsiveness
* Real-time travel APIs

Submit an issue or PR and let’s collaborate!

---

##  License

MIT License © 2025 prasannazzz

---

##  Mission Statement

> **This project is a step toward green travel tech.**
> By combining large language models with sustainability metrics, it helps travelers make smarter, planet-conscious decisions — without sacrificing experience.

 *Travel responsibly. Explore sustainably.*

```

---

Would you like me to:

- 🗂 Package all your project files into a `.zip`?
- 📤 Push it to a GitHub repo with commit messages?
- 🧑‍💻 Add GitHub Actions or badges (e.g., Streamlit deploy)?

Let me know what you'd like next!
```
