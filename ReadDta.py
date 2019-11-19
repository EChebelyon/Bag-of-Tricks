def read_dta(filepath):
    """
    A function to read dta, incase of duplicate value labels, map factor integer to string labels
    """
    import pandas as pd
    from pandas.io.stata import StataReader
    try:
        df = pd.read_stata(filepath)
    except ValueError:
        df = pd.read_stata(filepath , convert_categoricals=False)
        labels = pd.io.stata.StataReader(fp).value_labels()
        for variable, var_labels in labels.items():
            df.loc[:, variable] = df.loc[:, variable].map(var_labels, na_action="ignore")
    return df
