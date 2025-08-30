# 193 Valid Phone Numbers
grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt


# Breakdown:
# grep -E

# -E enables extended regular expressions (so you can use | for OR without escaping it).

# ^ ... $

# ^ → start of the line

# $ → end of the line

# Ensures the entire line matches the phone number pattern.

# (\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})

# The parentheses () group two alternatives:

# \([0-9]{3}\) [0-9]{3}-[0-9]{4}

# Matches a number like (123) 456-7890

# \( and \) match literal parentheses

# [0-9]{3} → three digits

# Space between area code and first three digits

# [0-9]{4} → last four digits

# [0-9]{3}-[0-9]{3}-[0-9]{4}

# Matches a number like 123-456-7890

# file.txt

# Input file to search for matching phone numbers.