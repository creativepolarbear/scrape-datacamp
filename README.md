# Scrape HTML and convert to Rmarkdown
``` sh
Rscript -e "install.packages(c('tidyverse', 'rvest', 'remotes'))"
Rscript scrape.R
pandoc --from html-native_divs-native_spans scrape.html --to gfm -o notebook.Rmd --no-highlight
```

# Convert Rmarkdown to Jupyter Notebook
``` sh
Rscript -e "install.packages('remotes')"
Rscript -e "remotes::install_github('mkearney/rmd2jupyter')"
Rscript -e "rmd2jupyter::rmd2jupyter('notebook.Rmd')"
```
