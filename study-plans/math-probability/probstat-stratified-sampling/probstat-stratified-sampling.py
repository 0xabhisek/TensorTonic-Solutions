def stratified_sample(strata_means, strata_stds, strata_sizes, total_sample):
    """Returns: dict with 'allocations' (list), 'stratified_mean', 'stratified_se' as floats."""
    total_pop = sum(strata_sizes)
    weights = [n / total_pop for n in strata_sizes]
    allocations = [max(1, round(w * total_sample)) for w in weights]
    strat_mean = round(sum(w * m for w, m in zip(weights, strata_means)), 4)
    strat_var = sum((w * s)**2 / a for w, s, a in zip(weights, strata_stds, allocations))
    strat_se = round(strat_var**0.5, 4)
    return {"allocations": allocations, "stratified_mean": strat_mean, "stratified_se": strat_se}
