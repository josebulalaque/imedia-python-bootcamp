# Programming Bootcamp

**By Stephen Singer**

## Introduction

This repository contains original learning materials, hands-on exercises, and code examples for a **Python Programming
Fundamentals** course.

It is structured for **complete beginners**, but can also serve as a **crash course for experienced developers** who
want to quickly get up to speed with Python. The program covers core syntax, control structures, data structures, and
object-oriented design — then branches into intermediate topics like file I/O, basic GUI development, and web
fundamentals.

Learning to program is not always easy. But the ability to break down problems, write logical solutions, and build
working software is one of the most rewarding and empowering skills you can develop today. This course was designed to
help you get there with structure, practice, and a bit of fun along the way.

By the end of the course, you should be able to:

- Read, write, and debug non-trivial Python programs
- Solve beginner to intermediate programming problems
- Build and understand small-scale software projects
- Decide which specific path in tech you'd like to pursue next

**Suggested flow:**

1. Read through the slides
2. Run and experiment with the sample code
3. Attempt the exercises
4. Review the labs or projects to apply what you've learned
5. Check your solution with the given solution and look for improvements

## Pacing

The material is designed for a **4-day bootcamp**:

- **9 hours/day**, with short breaks and longer lab periods
- Ideal for fast learners or those with prior coding experience

For absolute beginners, a **2-week pace** is recommended:

- **4 hours/day**, 5 days a week
- Allows for deeper review, repetition, and exploration

> You can also do both: finish the bootcamp at full speed, then revisit everything slowly with real-world projects.

## Course Outline

Each day contains slide decks, code samples, hands-on exercises, and lab activities.

| Day       | Topics                                                                     |
|-----------|----------------------------------------------------------------------------|
| **Day 1** | Introduction, input/output, variables, control flow, functions             |
| **Day 2** | Lists, tuples, dictionaries, sets, comprehension, strings, file handling   |
| **Day 3** | Classes, object-oriented programming principles, GUI programming (tkinter) |
| **Day 4** | Modules, libraries, best practices, web development introduction           |

## Getting Started

### Install Python

- [Download Python](https://www.python.org/downloads/)
    - ☑️ Enable "Add Python to PATH"
    - ☑️ Enable "Use admin privileges when installing py.exe"

### Install an Editor (Recommended: PyCharm)

- [Download PyCharm](https://www.jetbrains.com/pycharm/download/)
    - While any editor works (VS Code, Sublime, etc.), all examples here are aligned with PyCharm for consistency.

### Console Essentials (Optional)

### Running Python

If you're not using PyCharm, you can run any `.py` file with:

```bash
python filename.py
```

On macOS/Linux, use:

```bash
python3 filename.py
```

To open an interactive shell:

```bash
python
# or
python3
```

### Package Management

To avoid version conflicts, create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

Then install packages as needed:

```bash
pip install flask
```

### Clone the Repository

1. Sign up at [GitHub](https://github.com) and fork this repository.
2. In PyCharm:
    - Click **"Get from Version Control"**
    - Paste your fork URL
    - Log in with your GitHub account if prompted
3. When asked to configure interpreter:
    - Add a **local Python interpreter** via "Add Python Interpreter" → OK

> A visual guide is available in
> the [Day 1 Slides](https://github.com/Ayumu098/python-bootcamp/blob/master/slides/Day%2001%20-%20Introduction%20to%20Python%20and%20Basic%20Syntax.pdf)

Alternatively, if you're comfortable with Git:

```bash
git clone https://github.com/Ayumu098/python-bootcamp.git
```

Then open the folder in your preferred editor.

## Prerequisites

- Basic computer skills (navigating folders, installing software)
- Curiosity, patience, and a willingness to learn by doing
- No prior programming experience needed

## External Materials & Further Reading

### Python Fundamentals

- [Python Official Docs](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)
- [Python Tutor (Code Visualizer)](https://pythontutor.com/)

### Recommended Books

- *Automate the Boring Stuff with Python* – Al Sweigart
- *Python Crash Course* – Eric Matthes
- *Fluent Python* – Luciano Ramalho

### Interactive Practice

- [Exercism Python Track](https://exercism.org/tracks/python)
- [HackerRank Easy Problems](https://www.hackerrank.com/domains/python?filters%5Bdifficulty%5D%5B%5D=easy)
- [LeetCode Beginner Problems](https://leetcode.com/problemset/all/?difficulty=Easy)

## What's Next

After completing this bootcamp, try:

- A [100 Days of Code](https://www.100daysofcode.com/) challenge
- Building a personal project (blog, tracker, automation tool)
- Contributing to a
  beginner-friendly [open-source project](https://github.com/search?q=label%3Agood-first-issue&type=issues)
- Exploring specializations: data science, web dev, game dev, automation

### Bonus Content

See the bonus folder for:

- Functional programming
- OpenPyXL (Excel automation)
- Pandas (data science)
- Streamlit (simple web apps)
- BeautifulSoup (web scraping)

These aren't covered in-depth during the bootcamp, but they are excellent warmups.

### Sample Projects to Explore

These beginner/intermediate projects are great for practice:

- [Pygame Tutorial](https://github.com/techwithtim/Pygame-Tutorials)
- [Tkinter Collection](https://github.com/Aashishkumar123/Python-GUI-Project)
- [Flask Blog App](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog)
- [Other Mini Projects](https://github.com/Python-World/python-mini-projects)

### Packaging Python Applications

Packaging Python as Executables / Apps

You can ship Python programs as .exe (Windows) or runnable apps (Mac/Linux) so users don’t need Python installed.

#### PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile your_script.py
```

- Output: `dist/your_script.exe` (or binary).
- Docs: [PyInstaller Manual](https://pyinstaller.org/en/stable/?utm_source=chatgpt.com)

#### cx_Freeze

```bash
pip install cx_Freeze
cxfreeze your_script.py --target-dir dist/
```

- Output: folder with executable.
- Docs: [cx_Freeze Docs](https://cx-freeze.readthedocs.io/en/stable/?utm_source=chatgpt.com)

#### py2exe (Windows-only)

```bash
pip install py2exe
python setup.py py2exe
```

Requires a `setup.py` script.

Docs: [py2exe Guide](https://www.py2exe.org/?utm_source=chatgpt.com)

## Feedback & Issues

If you encounter any bugs or have suggestions for improvement, feel free
to [open an issue](https://github.com/Ayumu098/python-bootcamp/issues).

Forking and adapting this repo for your own training sessions or learning goals is encouraged.

## Final Note

This bootcamp is a **starting point** — not a finish line. The goal is to build a strong mental model of how code works,
and to practice applying it until it becomes second nature.

Learning to code is tough. It’s frustrating, messy, and non-linear. But it’s also one of the most valuable, empowering
skills you can build — not just for your career, but for your confidence.

If you make it through, even once, you're already ahead of most people.

Good luck and happy coding

## License

This project is licensed under the [MIT License](LICENSE).  
Feel free to fork, modify, and use it for your own learning or teaching.
