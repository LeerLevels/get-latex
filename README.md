# Goal
Creating a neatly formatted string based on settings

# Usage Examples



```
getLatex(1234) 
==> $1{,}23 \cdot 10^{3}$

getLatex(0.003456, {"pre_comma_digits": 2, "num_significant": 3}) 
==> $34{,}6 \cdot 10^{-3}$

getLatex(1234, {"wrapper":"", "use_scientific": False}) 
==> 1234
```

# Defaults

```
{
  "use_scientific": True,
  "pre_comma_digits": 1,
  "num_significant": 3,
  "num_decimals": 2, # only for non-scientific formatting
  "wrapper": "$",
  "output_delimiter": "{,}"
}
  ```
