# *dancing jovial penguin*'s personal website

This is a quick overview of the tools I've used, the blogging process, and the navigation functionality of the website in addition to miscellaneous notes.

## Resources

While building this website and creating some of its graphics, I've used the following programs, all of which contain open-source excerpts though only Krita and Git explicitly claim to be free *(as in freedom)* software:

* Visual Studio Code (as a code editor)
* Krita (for drawing)
* Git (for version control)
* Neocities (to host the website and gain publicity)

## The blogging functionality

I write my blog posts on Google Documents. When I'm done and ready to share one with the public, I copy the entire writing, paste in into a new Markdown file (.md extension) in the top directory of the entire project, and edit the file to comply with Markdown syntax (`#` for h1, `##` for h2, etc.).

Later, I open the `md-to-html.py` file and set the `blog_name` variable to what the blog post is going to be titled. I run the Python file through the terminal, and the script generates a new HTML file in the `blogs/` directory with the Markdown content formatted within HTML elements.

Finally, I manually update the `index.html` file to list the blog post and upload the HTML file that contains the blog post and index page to Neocities. I delete the Markdown file, as it's no longer necessary.

## The navigation/section-switching functionality

This refers to the navigation bar in the index page of the website. While building this functionality, I didn't use JavaScript but a less conventional method with CSS solely. 

Exploiting the `~` operator (subsequent-sibling combinator) and `:target` pseudo-class in the CSS syntax and putting `#about`, the first section that appears when previewed, after all the sections in the source code of index made such an approach feasible.

## Notes

While the website is almost entirely open-source, only the first blog post I've published will remain tracked and committed for the sake of simplicity. I update the blog posts' writing every now and then, so I didn't want to fill my commit history with these updates.

Changes to stylesheets, scripts, and the index page will likely continue being committed, though not immediately after.

The Nyan cat GIF with the Progress Pride Flag as its trailer was happily taken from https://toyhou.se/19984181.my-silly-resources/25710755.pride-nyans among versions with many other beautiful pride flags. ♡

This project was brought to you thanks to the brilliant resistance and solidarity of the LGBTQ+ community. 💞