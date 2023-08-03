"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["hello"],
            "answer": 2
        },
        {
            "input": ["openai"],
            "answer": 4
        },
        {
            "input": ["typescript"],
            "answer": 2
        },
        {
            "input": ["a"],
            "answer": 1
        },
        {
            "input": ["b"],
            "answer": 0
        },
        {
            "input": ["aeiou"],
            "answer": 5
        },
        {
            "input": ["AEIOU"],
            "answer": 5
        },
        {
            "input": ["The quick brown fox"],
            "answer": 5
        },
        {
            "input": ["Jumps over the lazy dog"],
            "answer": 6
        },
        {
            "input": [""],
            "answer": 0
        },
    ],
    "Extra": [
        {
            "input": ["THIS IS AN UPPERCASE STRING"],
            "answer": 8
        },
        {
            "input": ["this string has multiple vowels... aeiouaeiouaeiou"],
            "answer": 23
        },
    ]
}