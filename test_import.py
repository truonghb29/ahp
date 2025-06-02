#!/usr/bin/env python3
"""
Test script for Excel import functionality
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import read_candidates_from_excel, read_matrix_from_excel

def test_candidate_import():
    """Test importing candidates from Excel"""
    print("Testing candidate import...")
    try:
        candidates = read_candidates_from_excel('test_candidates.xlsx')
        print(f"✓ Successfully imported {len(candidates)} candidates:")
        for i, candidate in enumerate(candidates, 1):
            print(f"  {i}. {candidate}")
        return True
    except Exception as e:
        print(f"✗ Error importing candidates: {e}")
        return False

def test_matrix_import():
    """Test importing matrix from Excel"""
    print("\nTesting matrix import...")
    try:
        matrix = read_matrix_from_excel('test_criteria_3x3.xlsx')
        print(f"✓ Successfully imported {len(matrix)}x{len(matrix[0])} matrix:")
        for i, row in enumerate(matrix):
            print(f"  Row {i+1}: {row}")
        return True
    except Exception as e:
        print(f"✗ Error importing matrix: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Excel Import Functionality")
    print("=" * 40)
    
    success1 = test_candidate_import()
    success2 = test_matrix_import()
    
    print("\n" + "=" * 40)
    if success1 and success2:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed!")
