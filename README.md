# 🏨 Moustache Escapes – Nearest Property API

This project is a backend API developed in **Python (FastAPI)** that helps the tele-calling team at [Moustache Escapes](https://www.moustachescapes.com/) find the nearest hotel properties (within 50km) based on a customer’s location query (city/state/area), even if the input contains minor typos or spelling errors.  

It is designed for **real-time usage**, providing **responses in under 2 seconds** to support fast-paced customer interactions.

---

## 🔍 Problem Statement

Moustache Escapes receives calls from customers who mention different places across India, and the tele-caller needs to quickly check whether there is a Moustache property near that location. The customer may spell the place wrong, and the system must still try to find the closest match. The API needs to:

- Accept a **location query** (e.g., "delih" or "bangalre").
- Handle minor **typos** or character swaps.
- Geocode the location using coordinates.
- Find properties within a **50km radius**.
- Return the **nearest properties or a friendly "no result" message**.

---

## ✅ Features

- 📍 Geocoding input location using `geopy` with Nominatim.
- 📦 Distance calculation with geodesic formulas.
- ✨ Fuzzy matching for typo correction using `fuzzywuzzy`.
- ⚡ FastAPI backend with sub-2-second response times.
- 📂 Organized, modular Python code.
- 🧠 Smart filtering and ranking of nearby properties.

---

## 🧠 Thought Process & Problem Breakdown

### What was your initial thought process?

Upon reading the problem, the key tasks became clear:

1. **Input processing**: Accept user queries and correct minor typos.
2. **Geocoding**: Convert human-readable location to coordinates.
3. **Distance filtering**: Compare geocoded coordinates with hotel locations.
4. **Response formatting**: Return sorted property list (if any).

So I broke it down into:

- Creating a static database of hotel properties with coordinates.
- Implementing a typo-tolerant input parser.
- Connecting to a geocoder (Nominatim).
- Calculating haversine/geodesic distances.
- Building a clean API using FastAPI.

---

## 🛠️ Tools & Libraries Used

| Tool/Library | Why I Chose It |
|--------------|----------------|
| **FastAPI** | Lightweight, asynchronous, and perfect for fast APIs. |
| **geopy** | Provides simple access to geocoders and distance calculations. |
| **fuzzywuzzy** | Excellent for fuzzy string matching with good accuracy and performance. |
| **uvicorn** | ASGI server to serve the FastAPI application quickly. |
| **Python-Levenshtein** | Boosts `fuzzywuzzy`'s performance by accelerating string matching. |

Other options like Flask and Django were heavier or slower for rapid prototyping.

---

## 🧩 Key Challenge Faced

**Challenge:** Handling inaccurate user inputs (e.g., typos like `delih` for `Delhi`) while still giving meaningful location results.

**Solution:** I implemented **fuzzy matching** using `fuzzywuzzy` to correct queries to the most similar city name based on a curated list of Indian cities.

Additionally, **geocoding fails** were gracefully handled using error-checking and fallbacks.

---

## 💡 Future Improvements

If I had more time, I would explore:

- 🔍 **Autocomplete + Suggestions**: Return "Did you mean?" suggestions when the confidence is low.
- 🧠 **LLM-enhanced parsing**: Use OpenAI or Groq LLM APIs for semantic understanding of queries.
- 🗺️ **Caching geocoding results**: Avoid hitting Nominatim too frequently.
- 📦 **Database integration**: Move from in-memory data to a proper Postgres or MongoDB for scalability.
- 📈 **Logging and analytics**: To analyze queries and improve system intelligence over time.

These additions would significantly improve performance, scalability, and user experience.

---

