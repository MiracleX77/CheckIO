def switch_dict(data: dict[str, str]) -> dict[str, str]:
    dict_switch={}
    list_value = list(data.keys())
    list_key = list(data.values())
    for i in range (len(list_key)):
        if list_key[i] not in dict_switch.keys():
            dict_switch.update({list_key[i]:{list_value[i]}})
        else:
            dict_switch[list_key[i]].add(list_value[i])
    return dict_switch
switch_dict({"rouses": "red", "car": "red", "sky": "blue"})