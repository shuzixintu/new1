#!/usr/bin/env python3
"""
Main entry point for the calculator application.
"""

from calculator import Calculator


def main():
    """Run the calculator application."""
    calc = Calculator()
    
    print("Welcome to the Calculator!")
    print("=" * 40)
    
    # Demonstrate basic operations
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    
    print("=" * 40)
    print("Calculator demo complete!")


if __name__ == "__main__":
    main()
