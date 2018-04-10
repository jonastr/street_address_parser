# CODE CHALLENGE

We kindly ask you to solve the following code challenge as part of our selection process.

## Addressline

An address provider returns addresses only with concatenated street names and numbers. Our own system on the other hand has separate fields for street name and street number.

**Input:** string of address

**Output:** string of street and string of street-number

1. Write a simple program that does the task for the most simple cases, e.g.
   1. `"Winterallee 3"` -> `{"Winterallee", "3"}`
   1. `"Musterstrasse 45"` -> `{ "Musterstrasse", "45"}`
   1. `"Blaufeldweg 123B"` -> `{"Blaufeldweg", "123B"}`

2. Consider more complicated cases
   1. `"Am Bächle 23"` -> `{"Am Bächle", "23"}`
   1. `"Auf der Vogelwiese 23 b"` -> `{"Auf der Vogelwiese", "23 b"}`

3. BONUS: Consider other countries (complex cases)
   1. `"4, rue de la revolution"` -> `{"rue de la revolution", "4"}`
   1. `"200 Broadway Av"` -> `{"Broadway Av", "200"}`
   1. `"Calle Aduana, 29"` -> `{"Calle Aduana", "29"}`
   1. `"Calle 39 No 1540"` -> `{"Calle 39", "No 1540"}`

**Your Task:**

Write a running application in the programming language of your choice including test cases.
