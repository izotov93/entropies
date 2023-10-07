# Entropy calculation

## Installation

To install the package run the following command:
```
pip install -r requirements.txt
```

## Run calculations

Run command:
```
python entropies.py
```
The calculation configuration is specified in the base_config dictionary
* params - serial number of used entropy
* entropy_params - Parameters for calculations
* input_file - path to the file containing the series for which the entropy will be calculated


## Entropy used
### [Package - Antropy](https://github.com/raphaelvallat/antropy "github.com")
#### 1. Singular Value Decomposition entropy (SVD). [Documentation](https://raphaelvallat.com/entropy/build/html/generated/entropy.svd_entropy.html)

#### 2. Permutation entropy (Perm). [Documentation](https://raphaelvallat.com/entropy/build/html/generated/entropy.perm_entropy.html)

### [Package - EntropyHub](https://github.com/MattWillFlood/EntropyHub "github.com")

#### 3. Approximate entropy (ApEn). [Documentation](https://www.entropyhub.xyz/python/Functions/Base.html?highlight=app#EntropyHub.ApEn)

#### 4. Sample entropy (SampEn). [Documentation](https://www.entropyhub.xyz/python/Functions/Base.html?highlight=samp#EntropyHub.SampEn)

#### 5. Bubble entropy (BubbEn). [Documentation](https://www.entropyhub.xyz/python/Functions/Base.html?highlight=samp#EntropyHub.BubbEn)

#### 6. Cosine similarity entropy (CoSiEn). [Documentation](https://www.entropyhub.xyz/python/Functions/Base.html?highlight=samp#EntropyHub.CoSiEn)

#### 7.  Distribution entropy estimate (DistEn). [Documentation](https://www.entropyhub.xyz/python/Functions/Base.html?highlight=samp#EntropyHub.DistEn)

#### 8.  Fuzzy entropy (FuzzEn). [Documentation](https://www.entropyhub.xyz/python/Functions/Base.html?highlight=samp#EntropyHub.FuzzEn)

#### 9.  Phase entropy (PhasEn). [Documentation](https://www.entropyhub.xyz/python/Functions/Base.html?highlight=samp#EntropyHub.PhasEn)

### [Package - NNetEN](https://github.com/izotov93/NNetEn "github.com")

#### 10.  NNetEn entropy (NNetEn). [Documentation](https://github.com/izotov93/NNetEn#usage)
