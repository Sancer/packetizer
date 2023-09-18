import os

from packetizer.ast_utils import get_used_names
from packetizer.utils import convert_camel_case_to_snake_case


def write_class_files(classes, imports, output_dir):
    for class_name, class_content in classes.items():
        file_name = convert_camel_case_to_snake_case(class_name)
        file_path = f"{output_dir}/{file_name}.py"

        with open(file_path, "w") as f:
            for imp in imports:
                f.write(f"{imp}\n")
            f.write("\n")
            f.write(f"\n{class_content}\n")
            f.write("\n")

        used_names = get_used_names(file_path)

        with open(file_path, 'r') as f:
            lines = f.readlines()

        with open(file_path, 'w') as f:
            for line in lines:
                if line.startswith('import') or line.startswith('from'):
                    import_name = line.split()[1]
                    if import_name not in used_names:
                        continue
                f.write(line)


def write_init_file(class_dict, output_dir):
    with open(f"{output_dir}/__init__.py", "w") as f:
        for class_name in class_dict.keys():
            file_name = convert_camel_case_to_snake_case(class_name)
            f.write(f"from .{file_name} import {class_name}\n")


def write_to_files(class_dict, imports, output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    write_class_files(classes=class_dict, imports=imports, output_dir=output_dir)

    write_init_file(class_dict, output_dir)