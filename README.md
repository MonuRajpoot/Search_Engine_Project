# Search_Engine_Project

## Project Description – Web Page Similarity Checker using SimHash
 
### Project Overview

- This project compares the content of two different web URLs and determines how similar the two web pages are.

- The program extracts textual content from the web pages, generates their SimHash values, and then calculates the similarity percentage between them.


### Web Page Fetching

- The web page is downloaded using the requests library.

- The HTML content is parsed using BeautifulSoup.

- <script> and <style> tags are removed.

- Only the readable text content is extracted.

### Word Processing

- The text is converted to lowercase.

- Words are extracted using regular expressions.

- A custom hash value is generated for each word.

###  SimHash Calculation

-   A 64-bit SimHash value is generated for the document.
-   Each word’s hash contributes at the bit level to the final hash.

-   If the accumulated value at a bit position is positive, that bit becomes 1 in the final hash.

-   If the accumulated value is negative, that bit becomes 0.

-   This process produces a compact fingerprint that represents the entire document.

### Similarity Calculation

- Dono 64-bit hashes ko bit-by-bit compare kiya jata hai

-  Equal bits count kiye jate hain


-  Similarity=(CommonBits/64)×100
