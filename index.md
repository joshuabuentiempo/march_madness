## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/joshuabuentiempo/march_madness/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/joshuabuentiempo/march_madness/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.


# March Madness Bracket Predictor

## Webscraping

Used the Python web-scraping library BeautifulSoup4 to scrape data from https://www.sports-reference.com/cbb/.

Game data was pulled from each bracket starting in 2012 all the way to 2022.
ex. https://www.sports-reference.com/cbb/postseason/2018-ncaa.html

Each participating team had their season statistics pulled.
ex. https://www.sports-reference.com/cbb/schools/villanova/2018.html


## MySQL database

The scraped data was then stored into 2 different tables

"Games" table stored all of the game data (team a, team b, score of team a, score of team b, winner)
[Link](url) and ![Image](src)

"Teams" table stored all statistics for each participating team (fg, fga, ......, pts)
[Link](url) and ![Image](src)



## Analysis

Each game was analyzed be taking the difference of a statistic from team A and team B. (For this experiment, team A is always the team listed on
top). For example, let's say team A averaged 28 field goals made per game (fg) while team B only averaged 25 fg, then the difference would be 3.
(with team A as the reference)

  team A stat - team B stat = stat difference (with respect to the given game)


This difference was calculated for every game played and was tested for every team statistic.

### Binary Logistic Regression

To implement a binary logistic regression model,

**Data Visualizations**
Utilized Matplotlib package to graph the data for each variable

ex. PTS difference graph
[Link](url) and ![Image](src)

ex. stl difference graph
[Link](url) and ![Image](src)


### Linear Discriminant Analysis

**Data Visualizations**



## Results


