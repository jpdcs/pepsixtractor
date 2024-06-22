def extract_files(*.iso):
    with open(*iso, 'rb') as file:
        data = file.read()

    file_start_pattern1 = b'\xF2\x0D\xC9\x48\x61\x60\x60\x60\x63'

    file_start_index = 0
    file_number = 1

    while file_start_index < len(data):
        start_offset = data.find(file_start_pattern1, file_start_index)
        if start_offset == -1:
            break
   
        # Find the next occurrence of the start pattern
        next_start_offset = data.find(file_start_pattern1, start_offset + 1)
        
        # Determine the end offset based on the next occurrence of the start pattern
        end_offset = next_start_offset if next_start_offset != -1 else len(data)

        file_content = data[start_offset:end_offset]
        with open(f"K{file_number}.OKE", 'wb') as output_file:
            output_file.write(file_content)

        file_start_index = end_offset
        file_number += 1

    print(f"{file_number - 1} files extracted successfully.")

# Usage example
archive_path = 'megmid'  # Replace with your actual archive file path
extract_files(archive_path)