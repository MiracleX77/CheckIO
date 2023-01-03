def best_stock(data: dict[str, float]) -> str:
    return list(data.keys())[list(data.values()).index(max(data.values()))]
best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2})