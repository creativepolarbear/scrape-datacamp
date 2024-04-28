# Scrape HTML

``` sh
Rscript -e "install.packages(c('tidyverse', 'rvest', 'remotes'))"
Rscript scrape.R
```

# Convert HTML to Rmarkdown

``` sh
pandoc --from html-native_divs-native_spans scrape.html --to gfm -o notebook.md --no-highlight
```

# Convert Rmarkdown to Jupyter Notebook

``` sh
Rscript -e "install.packages('remotes')"
Rscript -e "remotes::install_github('mkearney/rmd2jupyter')"
Rscript -e "rmd2jupyter::rmd2jupyter('notebook.Rmd')"
```

# Convert Jupyter Notebook to Python script

``` sh
jupytext --to py notebook.ipynb   
```

# Remove comments

``` sh
sed -i -e '/# -/,/# +/d' notebook.py
```

# Style

``` sh
docker run -e RUN_LOCAL=true -v "$(pwd)":/tmp/lint github/super-linter
```
