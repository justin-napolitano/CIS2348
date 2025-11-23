---
slug: "github-cis2348"
title: "CIS2348"
repo: "justin-napolitano/CIS2348"
githubUrl: "https://github.com/justin-napolitano/CIS2348"
generatedAt: "2025-11-23T08:43:42.057256Z"
source: "github-auto"
---


# CIS2348 Project Overview and Technical Reference

## Motivation and Problem Statement

The CIS2348 repository serves as a practical compilation of programming exercises and projects designed to build and demonstrate foundational Python programming skills. The work systematically addresses common programming constructs such as input/output operations, control flow, data structures, sorting algorithms, file handling, and object-oriented programming. The final project focuses on integrating data from multiple CSV sources, a common real-world task in data processing and software development.

## Project Composition and Implementation Details

### Homework Assignments

The repository is organized into four homework folders (HW1 through HW4), each containing Python scripts that address specific programming problems or labs:

- **HW1:** Basic programming tasks including arithmetic operations, user input handling, and simple conditionals.
- **HW2:** More advanced topics such as string manipulation, regular expressions, file reading/writing, and basic algorithms (e.g., palindrome detection, exact change calculation).
- **HW3:** Introduction to object-oriented programming with classes modeling real-world entities (e.g., teams, items to purchase, food items). It also includes dictionary usage and menu-driven programs.
- **HW4:** More complex algorithms and data handling, including sorting algorithms (selection sort, quicksort), exception handling, and recursive function calls.

Each homework script generally follows a pattern of reading user input or files, processing data with Python constructs, and outputting results to the console or files.

### Final Project

The final project (in `FinalProjectPart1`) centers on processing and merging data from multiple CSV files:

- **Data Sources:** Manufacturer list, price list, and service dates, each stored in separate CSV files.
- **Data Integration:** The project reads these CSV files into dictionaries and lists, then performs merging operations based on a common key (`item_id`).
- **Data Structures:** Uses Python's `csv.DictReader` for parsing, and `defaultdict` for merging dictionaries efficiently.
- **Output:** The merged dataset combines manufacturer details, pricing, and service dates into a consolidated structure.

### Coding Practices and Style

- The code uses standard Python 3 syntax and libraries.
- Input validation and exception handling are present in some scripts, particularly in HW4.
- Object-oriented design is introduced in HW3 with classes encapsulating data and behavior.
- Some scripts include comments and TODOs indicating areas for further development or clarification.

## Practical Notes for Returning Developers

- **Running Scripts:** Ensure required input files are present in the working directory when running scripts that depend on external data.
- **Data Files:** The final project requires specific CSV files (`ManufacturerList.csv`, `PriceList.csv`, `ServiceDatesList.csv`) which are not included in the repository snapshot but are essential for execution.
- **Extensibility:** Many scripts are structured to allow easy addition of new features, such as expanding the menu options in the roster management program or enhancing sorting algorithms.
- **Error Handling:** Some scripts handle exceptions explicitly, but this is inconsistent; adding uniform error handling would improve robustness.
- **Code Documentation:** While some comments exist, comprehensive documentation is limited; consider adding docstrings and inline comments for maintainability.

## Summary

This repository is a methodical collection of Python programming exercises that progressively build competence in fundamental programming concepts and techniques. The final project applies these skills to a practical data integration task involving CSV files. The codebase is suitable for review, extension, and use as a reference for foundational Python programming patterns and practices.