import requests

# Ссылки на реестры Censor Tracker
sources = {
    "kz": "https://censortracker.github.io/ctconf/registry/kz.json",
    "ru": "https://censortracker.github.io/ctconf/registry/ru.json"
}

def convert():
    for country, url in sources.items():
        try:
            print(f"Processing {country}...")
            response = requests.get(url, timeout=10)
            data = response.json()
            
            # Сохраняем как обычный список доменов
            filename = f"{country}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                for domain in data:
                    f.write(f"{domain}\n")
            print(f"Successfully saved to {filename}")
            
        except Exception as e:
            print(f"Error processing {country}: {e}")

if __name__ == "__main__":
    convert()
