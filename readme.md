# Garden Path Sentences Analyzer

This project analyzes garden path sentences using the spaCy library in Python. Garden path sentences are grammatically correct sentences that lead readers to initially interpret them in one way, but require re-interpretation as they progress. The purpose of this project is to demonstrate the tokenization and named entity recognition capabilities of spaCy using a collection of garden path sentences.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

   ```shell
   git clone <repository-url>
   ```

2. Change to the project directory:

   ```shell
   cd garden-path-sentences-analyzer
   ```

3. Install the required dependencies:

   ```shell
   pip install spacy
   python -m spacy download en_core_web_sm
   ```

   This will install the spaCy library and the English language model required for the analysis.

## Usage

1. Import the `spacy` library:

   ```python
   import spacy
   ```

2. Load the English language model:

   ```python
   nlp = spacy.load('en_core_web_sm')
   ```

3. Define a list of garden path sentences:

   ```python
   gardenpathSentences = [
       "The complex houses married and single soldiers and their families.",
       "The horse raced past the barn fell.",
       "Mary gave the child a Band-Aid.",
       "That Jill is never here hurts.",
       "The cotton clothing is made of grows in Mississippi."
   ]
   ```

4. Iterate over each sentence and perform analysis:

   ```python
   for sentence in gardenpathSentences:
       doc = nlp(sentence)
       tokens = [token.text for token in doc]
       entities = [(ent.text, ent.label_) for ent in doc.ents]

       print("Sentence:", sentence)
       print("Tokens:", tokens)
       print("Entities:", entities)
       print("-" * 50)
   ```

5. Run the script and observe the analysis results.

## Examples

Here are some example garden path sentences that can be analyzed using this code:

1. "The old man the boats."
2. "The man whistling tunes pianos."
3. "The horse raced past the barn fell."

By running the code with these sentences, you can observe the tokenization and named entity recognition results.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the repository.