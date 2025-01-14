# Import required libraries and dependencies
import pandas as pd
from sklearn.cluster import KMeans


def get_elbow_dataframe(dataframe):
    """
    Accepts data frame.
    Calculate the k-value with range from 1-11
    n_init="auto" and random_state-3.
    Returns the dataframe with data to plot Elbow Curve.
    """
    # Create a list with the number of k-values to try
    # Use a range from 1 to 11
    k = list(range(1, 11))

    # Create an empty list to store the inertia values
    intertia = []

    # Create a for loop to compute the inertia with each possible value of k
    # Inside the loop:
    # 1. Create a KMeans model using the loop counter for the n_clusters
    # 2. Fit the model to the data using the scaled DataFrame
    # 3. Append the model.inertia_ to the inertia list
    for i in k:
        model = KMeans(n_clusters=i, n_init="auto", random_state=3)
        model.fit(dataframe)
        intertia.append(model.inertia_)

    # Create a dictionary with the data to plot the Elbow curve
    elbow_data = {"k": k, "inertia": intertia}

    # Create a DataFrame with the data to plot the Elbow curve
    elbow_df = pd.DataFrame(elbow_data)

    return elbow_df


if __name__ == "__main__":
    print(
        "This script should not be run directly! Import these functions for use in another file."
    )
