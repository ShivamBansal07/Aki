# Aki Quiz Bot

A Python-based quiz bot with a binary tree structure for decision-making.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Format](#file-format)
- [Contributing](#contributing)

## Introduction

This Quiz Bot is designed to facilitate decision-making through a binary tree structure. Users answer 'Yes' or 'No' to a series of questions, leading them to a final answer based on their responses.

## Features

- Interactive quiz with binary tree logic.
- Ability to load quiz data from a file.
- Tree traversal options: in-order, pre-order, post-order.
- Simple command-line interface.

## Installation

   ```bash
   git clone https://github.com/your-username/quiz-bot.git
   cd quiz-bot
   python quiz_bot.py
```
## Usage
Playing the Quiz:

Choose "P" to play the quiz. Answer questions with 'Y' or 'N' until you reach the final answer.
Loading a Different Game File:

Choose "L" and enter the file path or name to load a different set of quiz data.
Displaying Tree Traversal:

Choose "D" to display tree traversal options and explore the structure of the quiz tree.
Help:

Choose "H" to get help and learn more about the quiz.
Quitting:

Choose "X" to quit the quiz bot.

## File Format
The quiz data file should follow the format below:

```php
<data> <question>
<data> <question>
...
```
Example:

```
200 Are you a Coder? (Y/N)
150 Are you Well Paid? (Y/N)
120 You living the dream...
170 Us bro us...
250 Are you well paid? (Y/N)
220 Hire me...
270 Get a job...
```

## Contributing
Contributions are welcome! Feel free to open issues or pull requests for improvements or additional features.


