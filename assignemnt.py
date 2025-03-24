Assignment 1
Question: Capitalize the first letter of the given city names without using built-in functions like capitalize().
Cities Given: "jaranwala", "faislabad", "lahore"

Answer:

python
Copy
Edit
a = "jaranwala"
b = "faislabad"
c = "lahore"

cap1 = a[0].upper() + a[1:]
cap2 = b[0].upper() + b[1:]
cap3 = c[0].upper() + c[1:]

print(cap1, cap2, cap3)
Output:

nginx
Copy
Edit
Jaranwala Faislabad Lahore
Assignment 2
Question: Convert all first letters to uppercase and the rest to lowercase in a string without using capitalize().

Given: "Jaranwala Faislabad Lahore"

Answer:

python
Copy
Edit
a = "Jaranwala Faislabad Lahore"

formatted = a[0:1].lower() + a[1:9].upper() + " " + a[10:11].lower() + a[11:20].upper() + " " + a[20:21].lower() + a[21:].upper()

print(formatted)
Output:

nginx
Copy
Edit
jARANWALA fAISLABAD lAHORE
Assignment 3
Question: Replace the first letter of each word in the given string with a lowercase letter.

Given: "Jaranwala Faislabad Lahore Karachi Multan"

Answer:

python
Copy
Edit
st = "Jaranwala Faislabad Lahore Karachi Multan"
st = (st.replace("J", "j")
         .replace("F", "f")
         .replace("L", "l")
         .replace("K", "k")
         .replace("M", "m"))

print(st)
Output:

nginx
Copy
Edit
jaranwala faislabad lahore karachi multan
Assignment 4
Question: Reverse the order of city names in a list and capitalize the first and last letter of each word.

Given Cities:

python
Copy
Edit
Cities = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", 
          "Quetta", "Multan", "Rawalpindi", "Sialkot", "Hyderabad"]
Answer:

python
Copy
Edit
Cities = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", 
          "Quetta", "Multan", "Rawalpindi", "Sialkot", "Hyderabad"]

# Reverse the order
Cities.reverse()

# Capitalize first and last letter
formatted_cities = [x[0].upper() + x[1:-1].lower() + x[-1].upper() for x in Cities]

print(formatted_cities)
Output:

css
Copy
Edit
['HybAD', 'SialkoT', 'RawalindI', 'MultaN', 'QuettA', 'PeshawaR', 'FaisalabaD', 'IslamabaD', 