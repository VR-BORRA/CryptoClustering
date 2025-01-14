# Crypto Clustering

## Original Scaled Data

### Scaled Data Elbow Curve

<figure>
    <img src="images\scaledEC.png" alt="Scaled Curve">
</figure>

### The value of k is 4 from the above plot

### Scaled Scatter Plot

<figure>
    <img src="images\scaledScatterPlot.png" alt="Scaled Curve">
</figure>

## Principal Component Analysis

### The PCA explained ratio - [0.3719856 , 0.34700813, 0.17603793]

### The total explained variance of the three principal components is 0.89503166

### PCA Elbow Curve

<figure>
    <img src="images\pcaEC.png" alt="Scaled Curve">
</figure>

### The value of k is 4 from the above plot. This is same as scaled data k value.

### PCA Scatter Plot

<figure>
    <img src="images\pcaScatterPlot.png" alt="Scaled Curve">
</figure>

### Weights of Each Feature on each Principal Component

<figure>
    <img src="images\pcaWeightScore.png" alt="Scaled Curve">
</figure>

### The features having the strongest positive or negative influence on each component

|      | Positive                       | Negative                      |
|------|:------------------------------:|:-----------------------------:|
| PCA1 | price_change_percentage_200d   | price_change_percentage_14d   |
| PCA2 | price_change_percentage_30d    | price_change_percentage_1y    |
| PCA3 | price_change_percentage_7d     | price_change_percentage_30d   |