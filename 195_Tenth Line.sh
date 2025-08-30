# 195 Tenth Line
sed -n '10p' file.txt



# Breakdown:
# sed

# Stream editor for processing text.

# -n

# Suppresses automatic printing of each line.

# Without -n, sed prints every line by default.

# '10p'

# 10 → line number to operate on

# p → print the line

# So 10p → print only the 10th line

# file.txt

# Input file

# ✅ Example:
# file.txt:

# python-repl
# Copy code
# line1
# line2
# line3
# ...
# line10
# Command output:

# nginx
# Copy code
# line10
# 💡 Alternative using awk:

# bash
# Copy code
# awk 'NR==10' file.txt
# NR → current record (line) number

# Prints the 10th line only