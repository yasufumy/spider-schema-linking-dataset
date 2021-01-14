from argparse import ArgumentParser, FileType

from seqeval.metrics import classification_report


def get_tokens_and_tags(lines):
    tokens = []
    tags = []
    for line in lines.split("\n"):
        token, tag = line.split("\t")
        tokens.append(token)
        tags.append(tag)
    return tokens, tags


def main(args):
    pred = args.pred.read().split("\n\n")
    gold = args.gold.read().split("\n\n")
    Y_map = {}
    for y in gold:
        if y == "":
            continue
        y_tokens, y_tags = get_tokens_and_tags(y)
        Y_map[tuple(y_tokens)] = y_tags

    X = []
    Y = []
    for x in pred:
        if x == "":
            continue
        x_tokens, x_tags = get_tokens_and_tags(x)
        if "weigh" in x_tokens:
            x_tokens[x_tokens.index("weigh")] = "weight"
        assert tuple(x_tokens) in Y_map, x_tokens
        X.append(x_tags)
        Y.append(Y_map[tuple(x_tokens)])

    assert len(Y_map) == len(X) == len(Y)
    print(classification_report(Y, X))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--pred", type=FileType("r"), required=True, help="Predication (BIO format)")
    parser.add_argument("--gold", type=FileType("r"), default="", help="Gold standards")
    main(parser.parse_args())
