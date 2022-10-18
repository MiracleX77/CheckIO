
from collections.abc import MutableMapping

def flatten(d: MutableMapping, parent_key: str = '', sep: str ="/") -> MutableMapping:
    if d.get("empty")=={}:
        return {"empty":"{}"}
    items = []
    for k, v in d.items():
        # print("va = ",v)
        new_key = parent_key + sep + k if parent_key else k
        # print("new_key = ",new_key)
        if isinstance(v, MutableMapping) and v != {}:
            # print("1")
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            # print("2")
            if v =={}:
                items.append((new_key, ""))
            else:
                items.append((new_key, v))
    return dict(items)

print(flatten({"name": {
                         "first": "One",
                        "last": "Drone"},
                     "job": "scout",
                     "recent": {},
                     "additional": {
                         "place": {
                             "zone": "1",
                             "cell": "2"}}}))
flatten({"empty": {}})