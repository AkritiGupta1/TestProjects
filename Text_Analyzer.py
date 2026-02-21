#!/usr/bin/env python3
"""
Simple Text Analyzer
Analyzes a sentence to count words and characters
"""

def analyze_text(sentence):
    """
    Analyze text and return word count and character count.
    
    Args:
        sentence (str): The text to analyze
        
    Returns:
        dict: Contains 'words' and 'characters' counts
    """
    # Count words by splitting on whitespace
    words = len(sentence.split())
    
    # Count total characters (including spaces)
    total_chars = len(sentence)
    
    # Count characters without spaces
    chars_no_spaces = len(sentence.replace(" ", ""))
    
    return {
        'words': words,
        'total_characters': total_chars,
        'characters_without_spaces': chars_no_spaces
    }


def main():
    """Main function to run the text analyzer."""
    print("=" * 50)
    print("Simple Text Analyzer")
    print("=" * 50)
    
    # Get input from user with retry logic (max 5 attempts)
    sentence = None
    attempts = 0
    max_attempts = 5
    
    while not sentence:
        sentence = input("\nEnter a sentence: ").strip()
        
        if not sentence:
            attempts += 1
            if attempts >= max_attempts:
                print(f"Error: Maximum attempts ({max_attempts}) reached. Exiting program.")
                return
            print(f"Error: Please enter a valid sentence. Try again. (Attempt {attempts}/{max_attempts})")
            continue
    
    # Analyze the text
    results = analyze_text(sentence)
    
    # Display results
    print("\n" + "=" * 50)
    print("Analysis Results:")
    print("=" * 50)
    print(f"Number of Words: {results['words']}")
    print(f"Total Characters (with spaces): {results['total_characters']}")
    print(f"Characters (without spaces): {results['characters_without_spaces']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
