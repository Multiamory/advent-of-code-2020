import os
import configparser
import requests

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "advent_of_code.conf")


def get_input_for_day(file_path):
    """Returns the day's input string, either from a cached file or from the adventofcode website"""

    input_file_path = os.path.join(os.path.dirname(file_path), "input.txt")

    if os.path.exists(input_file_path):
        with open(input_file_path, "r") as f:
            return f.read()
    else:
        input_string = get_input_from_web(file_path)
        with open(input_file_path, "w") as f:
            f.write(input_string)
            return input_string


def get_input_from_web(file_path):
    """Returns the input values (as string) from the day's url (based on folder structure of the file_path"""

    cookies = {"session": get_session_id_from_config()}
    res = requests.get(get_day_url(file_path), cookies=cookies)

    if res.status_code == 200:
        return res.text
    elif res.status_code == 404:
        raise Exception(
            "Unable to retrieve input. Mostly likely this day's challenge has not yet been released\n"
            "(Or the folder structure is not correctly labeled with year and day)"
        )
    elif res.status_code == 500:
        raise Exception(
            "Something is wrong with your authentication. Mostly likely your session ID is incorrect.\n"
            "Run get_input.py in the root directory to update your session ID."
        )
    else:
        raise Exception(
            "Unknown error. If you are having trouble getting input values, you can copy\n"
            "and paste them into a file called input.txt in the day's folder."
        )


def get_session_id_from_config():
    """Returns the user's session ID from the advent_of_code.conf file."""
    try:
        config.read(config_path)
        session_id = config["Advent of Code"]["session"]
    except:
        session_id = ask_user_for_session_id()
        update_config(session_id)

    return session_id


def update_config(session_id):
    config["Advent of Code"] = {
        "session": session_id,
    }
    with open(config_path, "w") as config_file:
        config.write(config_file)


def ask_user_for_session_id():
    print(
        "You do not have a session ID set yet. Please enter it below and it will be saved in a file\n"
        "called advent_of_code.conf in the root directory.\n\n"
        "Go to adventofcode.com in your browser, login with any service you choose and open cookies.\n"
        "In Chrome hit F12, go to the 'application' tab, and select your cookie on the left panel.\n"
        "Copy the value, paste it here and press enter."
    )
    session_id = input("> ").strip()


def get_day_url(file_path):
    """Returns the input url based on a file's parent directories (for year and day)"""

    day = int(os.path.split(os.path.dirname(file_path))[1])
    year = os.path.split(os.path.dirname(os.path.dirname(file_path)))[1]

    return f"https://adventofcode.com/{year}/day/{day}/input"


if __name__ == "__main__":
    print(
        "This module is called from the scripts inside each folder.\n"
        "You can set your session ID here, though.\n"
        "Also, if you need to update your session ID you can do that here."
    )

    session_id = ask_user_for_session_id()
    if session_id:
        update_config(session_id)
