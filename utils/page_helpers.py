import pandas as pd
import os

def load_superstore_data(nrows=None):
    """Load the Superstore dataset from CSV file."""
    # Try multiple possible file paths
    possible_paths = [
        'data/Sample - Superstore.csv',
        './data/Sample - Superstore.csv',
        'Sample - Superstore.csv',
    ]
    
    # Try different encodings
    encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    
    for path in possible_paths:
        if os.path.exists(path):
            for encoding in encodings:
                try:
                    df = pd.read_csv(path, encoding=encoding, nrows=nrows)
                    # Clean column names
                    df.columns = df.columns.str.strip()
                    # Convert date columns
                    date_columns = [col for col in df.columns if 'date' in col.lower()]
                    for col in date_columns:
                        df[col] = pd.to_datetime(df[col], errors='coerce')
                    return df
                except (UnicodeDecodeError, Exception):
                    continue
    
    raise FileNotFoundError("Could not find Superstore dataset")
