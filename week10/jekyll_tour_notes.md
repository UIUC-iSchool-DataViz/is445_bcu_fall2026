---
title: Jekyll Tour Notes
layout: assignment
description: Tour of our Jekyll Template
---

## General Overview

The structure of important files in the template is shown below.  Note there are other files in several of the other directories, but this outlines the files we want to pay careful attention to.

```
<your github username>.github.io/
├── _data/
│   ├── programming-skills.yml
│   ├── other-skills.yml
│   └── timeline.yml
├── _example_posts/
├── _example_projects/
├── includes/
├── layouts/
├── _plugins/
├── _posts/
├── _projects/
│   └── 1_Vega_lite_project.md
├── assets/
│   ├── jsons/
│   └── pngs/
├── pages/
│   ├── projects.html
│   └── about.md
├── python_notebooks/
├── README.md
├── Gemfile
└── _config.yml
```

Note: some of this review is covered in the README found here: [https://github.com/jnaiman/online\_cv\_public](https://github.com/jnaiman/online_cv_public)

### Summary of commands

Here is the list of commands to reference for updating your page locally and pushing those changes to your remote github.io page.

#### Installation (already completed in course)

This should already be accomplished in Lab \#6 but in brief:
1. Create and clone a [github.io pages instance](https://docs.github.com/en/pages)
2. [Install](https://jekyllrb.com/docs/installation/) Ruby (~version 3.4) and Jekyll
3. [Download the template](https://github.com/jnaiman/online_cv_public), move files into your github.io pages instance locally
4. Install gems with `bundle install` in your local github.io pages directory

#### Serving files locally

Use `bundle exec jekyll serve` in your github.io directory to host your webpage (note you will have to manually refresh your webpage each time you modify your local files).

For "live" reloading instead use `bundle exec jekyll serve -l`.  Note: you can only use live reloads for one locally hosted page at a time (otherwise you will get a long and nebulous error).

**If you change the `_config.yml` file you will have to kill (`CTRL+C`) and restart the serve command.** All other files will automatically update changes to your locally served webpage if you use the `-l` option.

#### Pushing changes to your remote github.io  

For this you will use the same commands you used in Lab \#6 in the Terminal/Anaconda Prompt (make sure you have git installed\!):
  * `git pull` (ONLY IF you have edited things online in your repo)  
  * `git status` (to see changes)  
  * `git add -A` (add all changes)  
  * `git commit -m` "message" (commit changes)  
  * `git push` (push all changes)  

## Important Elements

Expand each element below to read more about each directory/file.

<details>
  <summary style="font-size: 22px;"><strong>_config.yml</strong></summary>


<p>This file is the first file we’ll really start modifying.  In this file you’ll see a lot of ways to modify the different parameters in your webpage.</p>

<img src="images/jekyll_tour/image3.png" width="80%" alt="Screenshot of the _config.yml file highlighting the first few comments at the top showing basic instructions for how to use this file to personalize the template webpage." style="border: 5px solid gray;">

<p>At the top you see some instructions of how to modify this page.  What we will do is fill in your new info, re-build the webpage with <code>bundle exec jekyll serve</code> to see our new webpage and then push these changes to our github.io pages repository when we are happy with those changes.</p>

<p>Let's try this by changing one thing first, the title – right now its "PossibleCorg", but you probably want something different!</p>

<img src="images/jekyll_tour/image23.png" width="80%" alt="Screenshot of the _config.yml file highlighting the 'title : PossibleCorg' line that needs to be modified with your name." style="border: 5px solid gray;">

<p>We'll walk through this, <b>but don’t do it yet</b> (we still need to update things for your page!)</p> 

<ul>
<li> Change this to "[Last Name] Resume"</li>
<li>Run <code>bundle exec jekyll serve</code> and see what happens locally  </li>
<li>Push to github, in the Terminal/Anaconda Prompt (make sure you have git installed!) do:</li>
<ul>  
  <li><code>git pull</code> (ONLY IF you have edited things online in your repo)  </li>
  <li><code>git status</code> (to see changes)  </li>
  <li><code>git add -A</code> (add all changes)  </li>
  <li><code>git commit -m "message"</code> (commit changes)</li>  
  <li><code>git push</code> (push all changes)  </li>
  <li>NOTE!!: if you have edited things online you will get a merge warning, you need to download your repository (<code>git pull</code>) and merge (<code>git merge</code>) and then commit this (<code>git commit -m</code>) – it will be easier if you do everything locally instead of using the GUI!  </li>
</ul>
<li>After some build time, your new Environment/Deployment with your changes will be updated on your github.io page (also see the "Actions" tab).</li>
</ul>

<p>This process takes a bit of a while to build to a full, hosted webpage, so generally, we’ll just host locally and check out some changes when we re-build and then we’ll push to our github.io repository when we have done enough changes.  Also! We haven’t updated things to point to your specific github page!  So this won’t work. Let’s work on that.</p>

<p>A few other items in this file that might be interesting to change:  </p>

<img src="images/jekyll_tour/image7.png" width="80%" alt="Screenshot of the _config.yml file highlighting the 'description : ' line that needs to be modified with your self description." style="border: 5px solid gray;">

<p>Update the description to say a little bit about yourself.</p>

<img src="images/jekyll_tour/image18.png" width="80%" alt="Screenshot of the _config.yml file highlighting the 'repository : ' line that needs to be modified with your GitHub user or repository name." style="border: 5px solid gray;">

<p>Make sure this points to <b>your</b> GitHub page!  This should be your user name (see the description).</p>

<p>Another thing you probably want to change in the future, is the link – if you want this as your main github.io page (i.e. where employers will “land” if they come to your github.io page) you can set the “baseurl” to just empty quotes “”:  </p>

<img src="images/jekyll_tour/image24_mod.png" width="80%" alt="Screenshot of the _config.yml file highlighting the 'baseurl : ' line that can be modified to point to a specific location." style="border: 5px solid gray;">
<p>Since we are still working on things, we’ll leave it as is and see that we need to add this part to the URL when we want to see our build on our github.io page.</p>

<p>Some other things we might want to change are our name, the image that we use for ourselves, and then any relevant links we want to appear as icons under our name:  </p>
<img src="images/jekyll_tour/image14.png" width="80%" alt="Screenshot of the _config.yml file highlighting the 'author : ' line and options below.  The name option updates your name, and the image option is modified to point to a URL where an image of you is kept.  Other options will add icons and links to various social media/other accounts (e.g., GitHub, linkedin, facebook, etc.)" style="border: 5px solid gray;">

<p>The last thing to check is that we are excluding files from our build that we don’t want included in our webpage.  You might have stuff stored in your github.io page other than this template and we don’t want to accidentally build this in into your page:</p>

<img src="images/jekyll_tour/image17.png" width="80%" alt="Screenshot of the _config.yml file highlighting the 'exclude : ' line and options below.  These list files that we don't want to have built into your final webpage (like the README.md, python_notebooks/, etc files and directories)." style="border: 5px solid gray;">
<p></p>
<p><b>Reminder: You can run an interactive version that will reload with your changes with <code>bundle exec jekyll serve -l</code> but it will crash if you have another interactive instance going.  You can always do <code>bundle exec jekyll serve</code> and then manually refresh to see your changes.</b></p>

</details>



<details>
  <summary style="font-size: 22px;"><strong>assets/</strong></summary>

<p>Inside the assets folder there are a few folders that we will add things to.  In particular, we will store any screenshots/images in <code>assets/pngs</code> and any vega-lite output JSON’s in the <code>assets/json</code> folder.  More on this when we get to making interactive plots on our webpage.  </p>
<img src="images/jekyll_tour/image27_mod.png" width="80%" alt="Screenshot of the directory structure of the template.  The assets/ directory is highlighted, and when listed (with ls command on a Mac/Linux) we see the png/ and json/ directories highlighted as well." style="border: 5px solid gray;">

</details>


<details>
  <summary style="font-size: 22px;"><strong>python_notebooks/</strong></summary>

<img src="images/jekyll_tour/image2_mod.png" width="80%" alt="Screenshot of the directory structure of the template.  The python_notebooks/ directory is highlighted, and when listed (with ls command on a Mac/Linux) we see the README.md with directions for how to use the directory and a test_generate_plots.ipynb notebook that is an example of a Python notebook that can be stored in this folder." style="border: 5px solid gray;">
<p>This is where you can store “loose” python notebooks.  In theory, you will link to your analysis plots in whatever repositories are storing those analysis notebooks, but just in case you want to do something “quick and dirty” and link that notebook, you can put it here.  Check out the <a href="https://github.com/jnaiman/online_cv_public/tree/main/python_notebooks">README</a> for updates, but that is the gist of this folder </p>
</details>

<details>
  <summary style="font-size: 22px;"><strong>pages/about.md</strong></summary>

<p>Also in the pages directory is a file where you can modify some things for your “About” page.  In particular, you can modify your description a that appears at the top by editing the about.md file in a text editor:  </p>
<img src="images/jekyll_tour/image4.png" width="80%" alt="Screenshot of the pages/about.md file opened in an emacs editor.  Yaml snippet is at the top and the rest of the page is written in a combination of markdown, HTML, and Liquid." style="border: 5px solid gray;">
<p>In particular, you want to edit all the stuff above the <code>\<div class...\></code> stuff (there are other files to edit for your skills section and your timeline!!).</p>

</details>

<details>
  <summary style="font-size: 22px;"><strong>_data/programming-skills.yml</strong></summary>

<img src="images/jekyll_tour/image26.png" width="70%" alt="Screenshot of the _data/programming-skills.yml file opened in an emacs editor.  Several yaml snippets are shown which list various skills and proficiencies." style="border: 5px solid gray;">

<p>In this file, you can include your different <b>programming</b> skills along with your proficiency.  There are a few options to add something new:</p>

<ul>
<li>Name of language  </li>
<li>Percentage of “skill” obtained – this is a bit fuzzy, but you can think of it as the % of the bar on the top that increases/decreases  </li>
<li>The level – this is the text that will show up on the top  </li>
<li>The color – what color you want to make this object  </li>
<ul>
  <li>Where do these colors come from? Check out the file: <code>_sass/_variables.scss</code>  </li>
</ul>
</ul>

</details>

<details>
  <summary style="font-size: 22px;"><strong>_data/other-skills.yml</strong></summary>

<img src="images/jekyll_tour/image29.png" width="70%" alt="Screenshot of the _data/other-skills.yml file opened in an emacs editor.  Several yaml snippets are shown which list various skills and proficiencies." style="border: 5px solid gray;">

<p>This file is very similar to the programming skills file, except it is a good place to list your various other skills.</p>

</details>


<details>
  <summary style="font-size: 22px;"><strong>_data/timeline.yml</strong></summary>

<img src="images/jekyll_tour/image22.png" width="70%" alt="Screenshot of the _data/timeline.yml file opened in an emacs editor.  Several yaml snippets are shown which list various academic and professional appointments." style="border: 5px solid gray;">

<p>The final file you probably want to modify in the <code>_data</code> folder is your timeline.  For each entry you need:</p>

<ul>
<li>The title (is it a job, if so, what kind? Are you a student, if so what major?)  </li>
<li> The start-end dates  </li>
<li> A description (right now, the “standard” placeholder text)</li>
</ul>

<p>Note this is <b>ORDER DEPENDENT</b>.  If we wanted our most recent position to be on top, we can re-order this to put that on top.  Whatever order it is in this file is the order it will show up on your About page timeline.</p>
</details>


<details>
  <summary style="font-size: 22px;"><strong>_projects/</strong></summary>

<img src="images/jekyll_tour/image10.png" width="70%" alt="Screenshot of the template file structure with the contents of the _project/ directory listed (with a ls command on Mac/Linux).  A single example project is shown." style="border: 5px solid gray;">

<p>Finally, we have your projects directory – this is where we will spend the majority of our time.  Here we will add projects that include interactive data visualizations.  The template includes project 1, in a file called <code>1_Vega_lite_project.md</code> which is a basic vega-lite example.  </p>

<p>Note the formatting here – there is a <code>1_</code> to indicate we want this project to come first in our list as it shows up on our projects page!</p>

<p>If we open up this template file in a text editor:  </p>
<img src="images/jekyll_tour/image5.png" width="70%" alt="Screenshot of the the file _projects/1_Vega_lite_project.md opened in the emacs text editor.  The top shows a yaml snippet and the rest of the project page is written in a combination of Markdown and small snippets of HTML." style="border: 5px solid gray;">
<p>we see a few things - there are some yaml snippets at the top that change the name of the project, what tool tags you want to use, an image to show on the projects page and a description.</p>

<p><b>Of vital importance!  If you are using vega-lite to make interactive plots, you MUST include the <code>custom_js</code> lines!!!</b></p>

<p>Other than those specifics, the rest of the file will be mostly written in markdown, with the occasional use of <code>\<vegachart\></code> HTML tags that we will use to make interactive visualizations.</p>



</details>



<!-- LESS IMPORANT -->





## Less Important Elements

We won't be going over these in detail, they are listed below as reference (these are useful to reference if you're building a new site with your own template but want to include Altair/vega-lite plots).  Expand each element below to read more about each directory/file.

<details>
  <summary style="font-size: 22px;"><strong>README.md</strong></summary>

  <p>This file is where you can give anybody that stumbles across the repository a bit more info about the source code.  In a text editor, it will look something like:</p>

  <img src="images/jekyll_tour/image11.png" width="80%" alt="Screenshot of the README.md file from within an emacs text editor." style="border: 5px solid gray;">

  <p>Which, if you go to the <a href="https://github.com/jnaiman/online_cv_public">online_cv GitHub repository</a> gets rendered to:  </p>

  <img src="images/jekyll_tour/image15.png" width="80%" alt="Screenshot of how the README.md file looks when rendered on github at: https://github.com/jnaiman/online_cv_public" style="border: 5px solid gray;">

  <p>You will not generally have to modify anything in this file.</p>

</details>

<details>
  <summary style="font-size: 22px;"><strong>Gemfile</strong></summary>

<p>This file tells bundler what to install that is needed for our project.  In this case, some jekyll stuff and some github pages stuff.  </p>
 
  <img src="images/jekyll_tour/image19.png" width="80%" alt="Screenshot of how the Gemfile within the emacs text editor showing various gem-install commands." style="border: 5px solid gray;">

<p>When you run <code>bundle install</code> bundler takes this file and creates a <code>Gemfile.lock</code> with all of the specific versions of packages that are installed (we won't be looking at that but you can check yours out if you want).</p>

<p>You don’t need to generally modify this file unless packages become incompatible with your version of Ruby/Jekyll, but if you create your own webpage not using the template, you might have to install other packages.</p>

</details>


<details>
  <summary style="font-size: 22px;"><strong>_plugins/</strong></summary>

  <img src="images/jekyll_tour/image28_mod.png" width="80%" alt="Screenshot of how the directory structure of the template with the _plugins directory highlighted." style="border: 5px solid gray;">

<p>Some other interesting files to know about (but that you don’t need to edit) is the <code>_plugins</code> – this is where the code to do interactive visualizations with vega-lite (like vegachart_tags).  There are some other things listed here as well that we are really going to ignore. These plugins come from the <a href="https://github.com/4dcu-be/4dcu.be">4dcu-be Jekyll template</a>.</p>

</details>

<details>
  <summary style="font-size: 22px;"><strong>_layouts/</strong></summary>

  <img src="images/jekyll_tour/image1_mod.png" width="80%" alt="Screenshot of how the directory structure of the template with the _layouts directory highlighted, and when listed (with ls command on a Mac/Linux) we see several layout files including default.html, element.html, page.html, and post.html." style="border: 5px solid gray;">
<p>Another set of files that we won’t really mess with is the layouts in the _layouts folder.  These are ways to define different layouts for different kinds of pages.  How our different pages look is also modified by things in the <code>_includes</code> directory as well.</p>

</details>

<details>
  <summary style="font-size: 22px;"><strong>_includes/</strong></summary>

<p>This also includes some info about how different pages will look.  </p>
  <img src="images/jekyll_tour/image12_mod.png" width="80%" alt="Screenshot of how the directory structure of the template with the _includes directory highlighted, and when listed (with ls command on a Mac/Linux) we see several layout files and directories." style="border: 5px solid gray;">
<p>For example, if we look in the <code>_includes/projects</code> folder:  </p>
  <img src="images/jekyll_tour/image25.png" width="80%" alt="Screenshot of how the directory structure of the _includes/projects with the files index.html and project-card.html which determine how project cards look when our project files are rendered in to html." style="border: 5px solid gray;">
<p>We see how each project card will look is probably determined in the <code>project-card.html</code> file and the general projects page is determined with the <code>index.html</code></p>.

</details>


<details>
  <summary style="font-size: 22px;"><strong>_example_posts/ and _example_projects/</strong></summary>
  <img src="images/jekyll_tour/image8.png" width="80%" alt="Screenshot of how the directory structure of the template with the _example_projects/ and _example_posts/ directories.  Contents of each are listed (with ls command on a Mac/Linux) to see the full range of project and post examples." style="border: 5px solid gray;">
<p>These two folders contain some example projects and blog posts you can look at.  Since we’ll be building our own in a bit, we won’t focus on these now, but they are there for you to come back to look at after we’ve started building our own to get some ideas.</p>
</details>

<details>
  <summary style="font-size: 22px;"><strong>_posts/</strong></summary>
  <img src="images/jekyll_tour/image13.png" width="80%" alt="Screenshot of how the directory structure of the template with the _posts/ directory.  Contents is listed (with ls command on a Mac/Linux) showing a single example blog post." style="border: 5px solid gray;">
<p>This contains a placeholder blog post if you want to talk about new things in your life, i.e. in a blog style.  Note the format of these with the filename starting with YYYY-MM-DD (year, month, date).</p>

<p>If you open this file up in a text editor, you’ll see that its mostly markdown:  </p>
  <img src="images/jekyll_tour/image21.png" width="80%" alt="The single blog post in the _posts/ directory opened with the emacs text editor.  Top show yaml structure and rest of post is written in Markdown." style="border: 5px solid gray;">
<p>With some yaml lines at the top that give specific parameters for each blog post, like title, any tags, color, etc.  See the <code>_example_posts/</code> directory for more examples.  </p>

<p>We won’t be focusing on blog posts for this class, but you can certainly check out the examples to get started if you want to blog.  <b>To add blogs to your page make sure to comment out the <code>- pages/blog.html</code> line in the <code>_config.yml</code> file.</b></p>

</details>

<details>
  <summary style="font-size: 22px;"><strong>_pages/projects.html</strong></summary>
<p>One small thing we might want to change in the pages directory – this is the <code>projects.html</code> file in which we can add github projects that are already <b>under your github name</b>.</p>

  <img src="images/jekyll_tour/image20.png" width="80%" alt="The _pages/projects.html file opened with the emacs text editor.  Top show yaml structure and rest of with the remote_projects location highlighted where one can update to point to remote projects stored on in their main GitHub." style="border: 5px solid gray;">

<p>In the example I’ve got the name of the repository that is associated with my main github page.  For reference, the URL of this repo is: </p>

<p><code>https://github.com/jnaiman/is507_spring2021</code></p>

<p>This shows up as an “automatic” card under our projects folder.  You won’t see <b>my</b> repository, even though it is included in the template you are using since it is not related to your repo!</p>
</details>

<p>
<p>That is the end of our overview!  Now we will dig a bit deeper into how to add projects and how to include vega-lite to make some interactive plots.  To do this, start with the vega-editor to make a quick example, then move to Python to start translating some of the stuff we’ve done on Starboard into this format.</p>

<p>Vega-lite-ho!</p>

