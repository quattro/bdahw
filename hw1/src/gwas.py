#! /usr/bin/env python
import argparse as ap
import os
import sys

import numpy as np
import scipy.stats as stats


def main(args):
    argp = ap.ArgumentParser(description="")
    argp.add_argument("geno", type=ap.FileType("r"))
    argp.add_argument("pheno", type=ap.FileType("r"))
    argp.add_argument("out_prefix")
    argp.add_argument("-o", "--output", type=ap.FileType("w"),
                      default=sys.stdout)

    args = argp.parse_args(args)

    ys = np.loadtxt(args.pheno)

    bcf = 382 * 4
    pvals = [[] for _ in range(4)]
    lines = args.geno.readlines()

    found = 0
    for idx, y in enumerate(ys.T):
        for sdx, line in enumerate(lines):
            snp = np.array(list(line.strip()), dtype=float)
            beta, bias, rho, pval, stderr = stats.linregress(snp, y)
            pvals[idx].append(pval)
            if pval < 0.05 / bcf:
                print idx + 1, sdx + 1, pval
                out = np.concatenate([np.c_[y], np.c_[snp]], axis=1)
                fname = "{}.{}.dat".format(args.out_prefix, found)
                np.savetxt(fname, out, fmt="%s")
                found += 1

    pvals = np.array(pvals)
    np.savetxt(args.output, pvals.T, fmt="%s")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
