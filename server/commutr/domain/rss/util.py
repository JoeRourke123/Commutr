import re


def get_rss_entry_data(entry_key: str, entry: dict) -> any:
    if entry_key is None:
        return None

    split_entry_key = entry_key.split(".")
    updated_entry = entry

    for index, key in enumerate(split_entry_key):
        if key not in updated_entry and key[:-2] not in updated_entry and key[:-3] not in updated_entry:
            raise KeyError(f"Could not find '{key}' from '{entry_key}' in {updated_entry}")

        remaining_key = '.'.join(split_entry_key[index + 1:])

        pattern = re.compile(r'([^\[]+)(?:\[(.*?)\])?')
        match = pattern.match(key)

        key = match.group(1)
        key_list_index = match.group(2)

        updated_entry = updated_entry[key]

        if key_list_index == '':
            return list(map(lambda e: get_rss_entry_data(remaining_key, e), updated_entry))
        elif key_list_index is not None:
            updated_entry = updated_entry[int(key_list_index)]

    return updated_entry


if __name__ == "__main__":
    print(get_rss_entry_data("first.second[].third", {
        "first": {
            "second": [
                {"third": {"hello": "there"}},
                {"third": "value2"},
                {"third": "value4"}
            ]
        }
    }))
