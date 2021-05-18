from argparse import ArgumentParser
from nlprep.nlp import NLPWriter, NLPRow
from nlprep.case_transform import CaseTransform

def _init_args():
    parser = ArgumentParser(
                        description="CTM format to NLP format")
    parser.add_argument('CTM', type=str,
                        help="Path to CTM file")
    parser.add_argument('NLP', type=str,
                        help="Path to NLP file")
    return parser.parse_args()


if __name__ == '__main__':
    args = _init_args()
    with open(args.CTM, 'r', encoding='utf-8') as ctmfile:
        with open(args.NLP, 'w', encoding='utf-8') as nlpfile:
            nlp_rows = []
            for line in ctmfile:
                _, _, ts, dur, token, _ = line.strip().split()
                nlp_rows.append(NLPRow.from_dict({'token': token,
                                                  'speaker': 1,
                                                  'ts': float(ts),
                                                  'endTs': round(float(ts) + float(dur), 3)}, 'token'))
            _case_label = "case"
            _label_ca = "CA"
            _label_uc = "UC"
            _label_mc = "MC"
            _label_lc = "LC"
            case_info = CaseTransform(nlp_rows,
                                     case_header=_case_label,
                                     label_ca=_label_ca,
                                     label_uc=_label_uc,
                                     label_mc=_label_mc,
                                     label_lc=_label_lc)

            nlp_rows = list(case_info.get_output())

            writer = NLPWriter(nlpfile, ['token', 'speaker', 'ts', 'endTs', 'punctuation', 'case', 'tags'], extrasaction='ignore')
            writer.writeheader()
            writer.writerows(nlp_rows)
