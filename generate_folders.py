import os
from files_renamer import rename_files


PLACEHOLDER = "XX"
START_DAY = 1
END_DAY = 24
TEMPLATE_DIR = "day XX"


def main(placeholder, start_day, end_day, template_dir):
    # Make a copy of the template directory and its contents and rename
    # the placeholder in the new directory to the day number
    for day_num in range(start_day, end_day + 1):
        new_dir = template_dir.replace(placeholder, str(day_num))
        os.mkdir(new_dir)
        os.system("cp -r " + template_dir + "/* " + new_dir)
        rename_files(new_dir, placeholder, str(day_num))


if __name__ == "__main__":
    main(PLACEHOLDER, START_DAY, END_DAY, TEMPLATE_DIR)
