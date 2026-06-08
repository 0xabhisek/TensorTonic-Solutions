def standard_errors(samples):

    r = lambda x: round(float(x), 4)

    se = []

    for sample in samples:

        sample = np.array(sample, dtype=float)

        se_i = np.std(sample, ddof=1) / np.sqrt(len(sample))

        se.append(r(se_i))

    mean_se = r(np.mean(se))

    return {
        "standard_errors": se,
        "mean_se": mean_se
    }

    