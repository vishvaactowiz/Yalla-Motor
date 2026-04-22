from request import request
import json
import time
from db import create_table, insert_data
from validate import State
from pydantic import ValidationError

city_api = "https://www.kia.com/api/kia2_in/findAdealer.getStateCity.do"
dealer_api = "https://www.kia.com/api/kia2_in/findAdealer.getDealerList.do"

response = json.loads(request(city_api))

data_map = {}

for state_obj in response["data"]["stateAndCity"]:
    state_key = state_obj["val1"]["key"]
    state_name = state_obj["val1"]["value"]

    if state_key not in data_map:
        data_map[state_key] = {
            "state_name": state_name,
            "state_code": state_key,
            "cities": {}
        }

    for city in state_obj["val2"]:
        city_key = city["key"]
        city_name = city["value"]

        url = f"{dealer_api}?state={state_key}&city={city_key}"

        try:
            dealer_json = json.loads(request(url))
            dealers = dealer_json.get("data", [])

            if city_key not in data_map[state_key]["cities"]:
                data_map[state_key]["cities"][city_key] = {
                    "city_name": city_name,
                    "city_code": city_key,
                    "stores": []
                }

            for d in dealers:
                full_address = " ".join(
                    filter(None, [
                        d.get("address1"),
                        d.get("address2"),
                        d.get("address3")
                    ])
                ).strip()

                store = {
                    "id": d.get("id"),
                    "store_name": d.get("dealerName"),
                    "url": d.get("website"),
                    "full_address": full_address,
                    "phone1": d.get("phone1"),
                    "dealer_type": d.get("dealerType")
                }

                data_map[state_key]["cities"][city_key]["stores"].append(store)
            print(state_key)    
            time.sleep(0.5)

        except Exception as e:
            print("Error:", state_key, city_key, e)


final_output = []

for state in data_map.values():
    state["cities"] = list(state["cities"].values())
    final_output.append(state)

rows = []

for state in final_output:
    for city in state["cities"]:
        for store in city["stores"]:
            rows.append((
                state["state_name"],
                state["state_code"],
                city["city_name"],
                city["city_code"],
                store["id"],
                store["store_name"],
                store["dealer_type"],
                store["phone1"],
                store["url"],
                store["full_address"]
            ))

create_table()

create_table()
insert_data(rows)

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=4, ensure_ascii=False)

from pydantic import ValidationError

validated_states = []

for state in final_output:
    try:
        valid_state = State(**state)
        validated_states.append(valid_state)

        print(f"\nState Validated: {valid_state.state_name} ({valid_state.state_code})")

        for city in valid_state.cities:
            print(f"   City: {city.city_name} ({city.city_code})")

            for store in city.stores:
                print(f"   Store: {store.id} | {store.store_name}")

    except ValidationError as e:
        print("\nValidation Error:")
        print(e.json())
