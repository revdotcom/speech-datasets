from argparse import ArgumentParser
from nlprep.nlp import text2nlp

def _init_args():
    parser = ArgumentParser(
                        description="TXT format to NLP format")
    parser.add_argument('TXT', type=str,
                        help="Path to TXT file")
    parser.add_argument('NLP', type=str,
                        help="Path to NLP file")
    return parser.parse_args()


if __name__ == '__main__':
    args = _init_args()
    text2nlp(args.TXT, args.NLP)
