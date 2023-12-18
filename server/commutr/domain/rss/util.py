import re


def get_rss_entry_data(entry_key: str, entry: dict) -> any:
    """
    For a given dict and RSS field key, we want to find the specific data.

    Keys can be:
        * `title`: Just gets the title field at the root of entry
        * `data.tags[].title` would get a list of the article's tag names, i.e. ['sport', 'football', 'Ronaldo']
        * `data.author[1].name` would return 'John Doe' as it is just returning the name of the 2nd author in the author list

    Args:
        entry_key: the RSS field key, in the format of: data.author[2].name which is equivalent to article['data']['author'][2]['name']
        entry: the dict to fetch this information from

    Returns:
        the found or mapped value from the article RSS data
    """
    if entry_key is None:
        # If we have no key, we cannot continue
        return None

    split_entry_key = entry_key.split(".")          # Split the key up into individual sections
    updated_entry = entry

    # For each section in the key, and the section's index
    for index, key in enumerate(split_entry_key):
        # Pattern to separate any index brackets in the key from the attribute name
        pattern = re.compile(r'([^\[]+)(?:\[(.*?)\])?')
        match = pattern.match(key)

        key = match.group(1)                # For author[2], returns just author
        key_list_index = match.group(2)     # For author[2], returns 2. For author[] returns '', for link returns None

        if key not in updated_entry:
            raise KeyError(f"Could not find '{key}' from '{entry_key}' in {updated_entry}")

        remaining_key = '.'.join(split_entry_key[index + 1:])

        updated_entry = updated_entry[key]

        if key_list_index == '':
            # If we are mapping the entire list, use recursion to get each value in the list
            return list(map(lambda e: get_rss_entry_data(remaining_key, e), updated_entry))
        elif key_list_index is not None:
            # If we have an index in the key, just continue searching only on that list element
            updated_entry = updated_entry[int(key_list_index)]

    # If no more keys are available, return what has been found
    return updated_entry


if __name__ == "__main__":
    # Just some test code to demonstrate...
    print(get_rss_entry_data("first.second[].third", {
        "first": {
            "second": [
                {"third": {"hello": "there"}},
                {"third": "value2"},
                {"third": "value4"}
            ]
        }       # Result: [{'hello': 'there'}, 'value2', 'value4']
    }))
