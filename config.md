<!--
Add here global page variables to use throughout your website.
-->
+++
import Dates

author = "Brady Planden"
short_author = "B. Planden"
description = "Brady Planden - Website"
mintoclevel = 2
maxtoclevel = 3

# defaults for layout variables
cover = false
content_tag = ""


# Add here files or directories that should be ignored by Franklin, otherwise
# these files might be copied and, if markdown, processed by Franklin which
# you might not want. Indicate directories by ending the name with a `/`.
# Base files such as LICENSE.md and README.md are ignored by default.
ignore = ["node_modules/"]

# RSS (the website_{title, descr, url} must be defined to get RSS)
generate_rss = false
website_title = "Brady Planden"
website_descr = "Portfolio Website"
website_url   = "https://bradyplanden.github.io/"

current_year = Dates.year(Dates.today())
+++

<!--
Add here global latex commands to use throughout your pages.
-->
\newcommand{\eqa}[1]{\begin{eqnarray}#1\end{eqnarray}}
\newcommand{\eqal}[1]{\begin{align}#1\end{align}}

\newcommand{\esp}{\quad\!\!}
\newcommand{\spe}[1]{\esp#1\esp}
\newcommand{\speq}{\spe{=}}

\newcommand{\E}{\mathbb E}
\newcommand{\R}{\mathbb R}
\newcommand{\eR}{\overline{\mathbb R}}

\newcommand{\scal}[1]{\left\langle#1\right\rangle}

<!-- ABI specific -->
\newcommand{\KL}{\mathrm{KL}}

<!-- optimisation specific -->
\newcommand{\xopt}{x^\dagger}
\newcommand{\deltaopt}{\delta^\dagger}
\newcommand{\prox}{\mathrm{prox}}

<!-- matrix theory specific -->
\newcommand{\inv}{^{-1}}

<!-- in-text replacements -->
\newcommand{\abi}[1]{/pub/csml/abi/!#1}
\newcommand{\cvx}[1]{/pub/csml/cvxopt/!#1}
\newcommand{\mth}[1]{/pub/csml/mtheory/!#1}
\newcommand{\uns}[1]{/pub/csml/unsorted/!#1}

<!-- Text decoration -->
\newcommand{\ul}[1]{~~~<span id=underline>!#1</span>~~~}
\newcommand{\htmlcolor}[2]{~~~<font color="!#1">!#2</font>~~~}

<!-- Text alignment -->
\newcommand{\br}{~~~</br>~~~} <!-- skip a line -->
\newcommand{\nobr}[1]{~~~<nobr>~~~#1~~~</nobr>~~~}
