import argparse
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def sample_function(name: str) -> str:
    """
    Sample function to demonstrate modularity.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the template repository."

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Template Python Application")
    parser.add_argument('--name', type=str, default='World', help='Name to greet')
    return parser.parse_args()

def main():
    """
    Main function to run the script.
    """
    args = parse_args()

    try:
        message = sample_function(args.name)
        logging.info(message)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()