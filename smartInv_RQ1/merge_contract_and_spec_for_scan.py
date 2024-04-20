import os
import shutil
import zipfile

from tqdm import tqdm


def process_and_zip_files_with_function_name(template_dir, contracts_dir):
    # Ensure the template directory exists
    if not os.path.exists(template_dir):
        print(f"Template directory {template_dir} does not exist.")
        return

    # Ensure the contracts directory exists
    if not os.path.exists(contracts_dir):
        print(f"Contracts directory {contracts_dir} does not exist.")
        return

    spec_files = [f for f in os.listdir(contracts_dir) if f.endswith(".spec")]

    # Create the "zips" directory if it doesn't exist
    zips_dir = "./zips"
    os.makedirs(zips_dir, exist_ok=True)

    for filename in tqdm(spec_files, desc="Processing .spec files"):
        # Remove the '.spec' extension before splitting
        filename_no_ext = filename[:-5]
        
        # Extract name, function name, and hash from the filename
        parts = filename_no_ext.split("_")
        if len(parts) < 4:
            print(f"Filename {filename} does not have the expected format.")
            continue

        name = parts[0]
        function_name = parts[1]
        hash_value = parts[3]

        # Create a new directory name with the function name included
        new_dir_name = f"{name}_{function_name}_{hash_value}"
        new_dir_path = os.path.join('.', new_dir_name)

        # Check if the directory already exists, if so, skip processing
        if os.path.exists(new_dir_path):
            print(f"Directory {new_dir_name} already exists. Skipping...")
            continue

        os.mkdir(new_dir_path)

        # Copy all files and directories from template directory to the new directory
        for item in os.listdir(template_dir):
            src_path = os.path.join(template_dir, item)
            dest_path = os.path.join(new_dir_path, item)

            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)
            else:
                shutil.copy(src_path, dest_path)

        # Copy and rename the .spec file
        spec_src = os.path.join(contracts_dir, filename)
        spec_dest = os.path.join(new_dir_path, "prover_verification.spec")
        shutil.copy(spec_src, spec_dest)

        # Zip the new directory
        zip_filename = f"{new_dir_name}.zip"
        zip_path = os.path.join(zips_dir, zip_filename)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for root, dirs, files in os.walk(new_dir_name):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), new_dir_name))

        print(f"Processed and zipped {filename} into {zip_path}")

# Define the directories
template_dir = "smartInv_RQ1/templates/template_anyswap"
contracts_dir = "smartInv_RQ1/specs/spec_anyswap"

# Call the function
process_and_zip_files_with_function_name(template_dir, contracts_dir)