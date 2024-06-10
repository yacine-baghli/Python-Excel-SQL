# Open the input file for reading
with open("requetes_sql.txt", "r") as infile:
    # Read the lines
    lines = infile.readlines()

# Open the output file for writing
with open("requetes_sql_2.txt.txt", "w") as outfile:
    # Iterate through the lines
    for line in lines:
        # Replace 'NULL' with '00m00'
        modified_line = line.replace("NULL", "'00m00'")
        # Write the modified line to the output file
        outfile.write(modified_line)
