import json


def convert_to_grams(masa):
    if "ct" in masa:
        return float(masa.replace("ct", "").replace(",", ".")) * 0.2
    if "g" in masa:
        return float(masa.replace("g", "").replace(",", "."))
    else:
        return 0


if __name__ == "__main__":

    # for zbior_wejsciowy.json
    with open(
        "simple_site-AKAI-/app/fixtures/website/dane.json", "r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    sorted_data = sorted(data, key=lambda x: convert_to_grams(x["Masa"]), reverse=True)

    print("Dla zbiór_wejściowy.json:")
    for i in range(5):
        print(sorted_data[i])


    # for kategorie.json
    with open(
        "simple_site-AKAI-/app/fixtures/website/categories.json", "r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    sorted_data = sorted(data, key=lambda x: x["Wartość za uncję (USD)"], reverse=True)

    print("\n\nDla kategorie.json:")
    for i in range(5):
        print(sorted_data[i])
