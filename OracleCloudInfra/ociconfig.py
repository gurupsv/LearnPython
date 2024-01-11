import configparser
import os


def parse_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    print("Available Sections:")
    for section in config.sections():
        print(f"- {section}")

    selected_section = input("Enter the section you want to print (or press Enter to print all): ")

    if selected_section:
        if config.has_section(selected_section):
            print(f"\n[{selected_section}]")
            for key, value in config.items(selected_section):
                print(f"{key}={value}")
        else:
            print(f"Section '{selected_section}' not found.")
    else:
        for section in config.sections():
            print(f"\n[{section}]")
            for key, value in config.items(section):
                print(f"{key}={value}")


if __name__ == "__main__":
    home_dir = os.environ.get("HOME")
    file_path = os.path.join(home_dir, ".oci/config")

    if os.path.isfile(file_path):
        parse_config(file_path)
    else:
        print(f"Config file not found: {file_path}")
