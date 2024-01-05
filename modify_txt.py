def modify_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Split the line at the first "=" sign
            parts = line.split("=", 1)
            
            if len(parts) == 2:
                package_name, rest_of_line = parts
                
                # Extract version and remove the rest after the next "=" sign
                version = rest_of_line.split("=", 1)[0]
                
                # Write the modified line to the output file
                outfile.write(f'{package_name}=={version}\n')
            else:
                # If the line does not contain "=", write it as is
                outfile.write(line)

if __name__ == "__main__":
    input_file_path = "requirements.txt"  # Change this to the actual path of your input file
    output_file_path = "reqiurements.txt"  # Change this to the desired output file path
    
    modify_lines(input_file_path, output_file_path)
