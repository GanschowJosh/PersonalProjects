import os
from pptx2md import convert

def convert_pptx_files_to_md(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pptx"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".md")

            convert(pptx_path=input_path, output=output_path)

if __name__ == "__main__":
    input_folder = input("Input folder:\t").replace("\\", "/") 
    output_folder = input("Output folder:\t").replace("\\", "/")

    convert_pptx_files_to_md(input_folder, output_folder)
